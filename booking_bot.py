import os
import time
import json
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from captcha_solver import solve_captcha


def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = r"""
 __  __                  _ _              _       
|  \/  | __ _ _   _ _ __(_) |_ __ _ _ __ (_) __ _ 
| |\/| |/ _` | | | | '__| | __/ _` | '_ \| |/ _` |
| |  | | (_| | |_| | |  | | || (_| | | | | | (_| |   
|_|  |_|\__,_|\__,_|_|  |_|\__\__,_|_| |_|_|\__,_|
    """
    print(banner)
    print("Unknown Dev: Wa.me/201286016083\n")


def load_config():
    try:
        with open("config.json", "r") as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        return None


def setup_driver():
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(service=service, options=options)


def determine_scope(driver):
    try:
        if "appointment_showDay" in driver.current_url:
            return "day"
        elif "appointment_showMonth" in driver.current_url:
            return "month"
        else:
            raise ValueError("Unable to determine scope")
    except Exception as e:
        print(f"Error determining scope: {e}")
        return None


def handle_captcha(driver, captcha_solver_url, scope):
    try:
        captcha_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, f"appointment_captcha_{scope}_captchaText"))
        )

        captcha_value = solve_captcha(driver, captcha_solver_url)
        if not captcha_value:
            print("CAPTCHA solving failed.")
            return False

        print(f"CAPTCHA solved: {captcha_value}")
        captcha_input.clear()
        captcha_input.send_keys(captcha_value)
        captcha_input.send_keys(Keys.RETURN)
        return True

    except TimeoutException:
        print("No CAPTCHA found, skipping.")
        return True
    except Exception as e:
        print(f"Captcha error: {e}")
        return False


def find_available_slot(driver):
    try:
        slots = driver.find_elements(By.XPATH, "//a[contains(@href, 'appointment_showForm.do')]")
        if slots:
            print(f"Found {len(slots)} slots.")
            return slots[0].get_attribute("href")
        return None
    except:
        return None


def process_url(url_info, config):
    category = url_info["category"]
    url = url_info["url"]
    form_data = config["form_data"]
    captcha_solver_url = config["captcha_solver_url"]

    driver = setup_driver()
    try:
        print(f"Checking: {url}")
        driver.get(url)
        time.sleep(2)

        scope = determine_scope(driver)
        if not scope:
            return

        if not handle_captcha(driver, captcha_solver_url, scope):
            return

        slot_link = find_available_slot(driver)
        if slot_link:
            print(f"Opening form...")
            driver.get(slot_link)

            if handle_captcha(driver, captcha_solver_url, "newAppointmentForm"):
                fill_final_form(driver, form_data)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()


def fill_final_form(driver, form_data):
    try:
        driver.find_element(By.ID, "appointment_newAppointmentForm_lastname").send_keys(form_data["lastname"])
        driver.find_element(By.ID, "appointment_newAppointmentForm_firstname").send_keys(form_data["firstname"])
        driver.find_element(By.ID, "appointment_newAppointmentForm_email").send_keys(form_data["email"])
        driver.find_element(By.ID, "appointment_newAppointmentForm_emailrepeat").send_keys(form_data["email"])
        driver.find_element(By.ID, "appointment_newAppointmentForm_fields_0__content").send_keys(form_data["passport"])

        driver.find_element(By.ID, "appointment_newAppointmentForm_appointment_addAppointment").click()
        print("Form submitted.")

    except Exception as e:
        print(f"Form error: {e}")


def check_slots():
    config = load_config()
    if not config:
        return

    threads = []
    for url_info in config["urls"]:
        t = threading.Thread(target=process_url, args=(url_info, config))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def main():
    print_banner()  # 👈 هنا بيطبع الشكل أول ما البرنامج يفتح
    print("Starting the bot...\n")
    check_slots()


if __name__ == "__main__":
    main()