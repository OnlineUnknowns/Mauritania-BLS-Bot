# 🚀 Mauritania BLS Appointment Bot

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Mauritania+BLS+Automation+Bot;Smart+Appointment+Booking+System;Fast+Reliable+Scalable+Automation" />

<br/>

<img src="https://img.shields.io/github/stars/OnlineUnknowns/Mauritania-BLS-Bot?style=for-the-badge"/>
<img src="https://img.shields.io/github/forks/OnlineUnknowns/Mauritania-BLS-Bot?style=for-the-badge"/>
<img src="https://img.shields.io/github/last-commit/OnlineUnknowns/Mauritania-BLS-Bot?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>

</div>

---

## ⚡ Overview

A high-performance automation system designed to intelligently monitor and book appointments on the **BLS Mauritania platform**.

Built with:
- Speed ⚡  
- Reliability 🧠  
- Scalability 🚀  

---

## 🧠 System Architecture

```mermaid
graph TD
A[User Config JSON] --> B[Automation Engine]
B --> C[Selenium Controller]
C --> D[BLS Website]

B --> E[Captcha Solver Module]
B --> F[Retry Engine]
B --> G[Logger System]

F --> C
G --> H[Reports & Logs]
```

---

## 🔄 How It Works

```mermaid
flowchart TD
A[Start Bot] --> B[Load Config]
B --> C[Open BLS Website]
C --> D[Check Availability]

D --> E{Slot Available?}

E -->|Yes| F[Fill Form Automatically]
F --> G[Solve CAPTCHA]
G --> H[Confirm Booking]
H --> I[Success ✅]

E -->|No| J[Wait & Retry]
J --> D
```

---

## ✨ Features

### ⚡ Core Automation
- Real-time appointment checking
- Auto booking workflow
- Smart retry mechanism

### 🔐 Intelligence Layer
- CAPTCHA solving (OCR / external services)
- Smart date filtering
- Adaptive navigation handling

### 📊 Monitoring System
- Live logging
- Debug mode support
- Full execution tracking

---

## 🛠 Tech Stack

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/chrome/chrome-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="50"/>

</div>

---

## 📂 Project Structure

```bash
Mauritania-BLS-Bot/
│
├── booking_bot.py
├── captcha_solver.py
├── config.json
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

```bash
git clone https://github.com/OnlineUnknowns/Mauritania-BLS-Bot.git
cd Mauritania-BLS-Bot
pip install -r requirements.txt
```

---

## ▶ Run

```bash
python booking_bot.py
```

---

## 📊 Live Workflow Status

```mermaid
flowchart LR
A[Idle] --> B[Checking Slots]
B --> C{Available?}
C -->|Yes| D[Booking Process]
C -->|No| E[Sleep Mode]
E --> B
D --> F[Success Log]
```

---

## 💎 Premium Version

<div align="center">

<a href="https://wa.me/201286669272">
<img src="https://img.shields.io/badge/Upgrade%20to%20Premium-WhatsApp-25D366?style=for-the-badge&logo=whatsapp"/>
</a>

</div>

### 🚀 Premium Includes:
- Ultra-fast execution engine  
- Advanced CAPTCHA solving  
- Priority updates  
- Smart AI retry system  
- Dedicated support  

---

## 📈 GitHub Analytics

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=OnlineUnknowns&show_icons=true&theme=tokyonight&hide_border=true"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=OnlineUnknowns&layout=compact&theme=tokyonight&hide_border=true"/>

</div>

---

## 👁 Visitor Counter

<div align="center">

<img src="https://komarev.com/ghpvc/?username=OnlineUnknowns&label=Visitors&color=blueviolet&style=for-the-badge"/>

</div>

---

## 📞 Contact

<div align="center">

<a href="mailto:Advinistrator@gmail.com">
<img src="https://img.shields.io/badge/Email-Support-red?style=for-the-badge&logo=gmail"/>
</a>

<a href="https://wa.me/201286669272">
<img src="https://img.shields.io/badge/WhatsApp-Chat-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/>
</a>

<a href="https://github.com/OnlineUnknowns">
<img src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github"/>
</a>

</div>

---

## ⭐ Support

[![Buy Me A Coffee](https://img.shields.io/badge/Support-Buy%20Me%20A%20Coffee-yellow.svg)](https://buymeacoffee.com/onlineunknowns)

------------------------------------------------------------------------

