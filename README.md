# 🎰 PyArcade Casino

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Playable-orange?style=for-the-badge)

> **A terminal-based Python project that simulates basic casino games to practice modular design, game logic, and state handling.**

---
## 🧭 Project Purpose

This project was built to practice and improve:

- Writing multi-file Python programs
- Implementing game logic and control flow
- Passing shared state (credits) between functions
- Refactoring repeated logic into reusable utilities
- Handling user input and errors in terminal applications

The project serves as a practical portfolio example of building a scalable, multi-module application in Python.

---

## 🎲 Welcome to PyArcade Casino

Step into a fully interactive terminal-based casino experience.  
You begin with **10,000 credits** — can you beat the house, or will you go bust?

---

## 📌 Overview

PyArcade Casino is a console-based casino simulator written in Python.  
The program allows a player to choose between different casino-style games while maintaining a shared credit balance across games.

It includes three complete games:

1. **🃏 Blackjack** — Dealer logic, hit/stand logic, Ace handling, 2.5× blackjack payout  
2. **🎰 Slots** — Weighted probability reels, tiered payouts, jackpots  
3. **🔴 Roulette** — European-style wheel (0–36) with multiple betting strategies  

All games are coordinated by a **central casino engine** that manages credits, session flow, and game routing.

---

## 🚀 Key Features

- 🎮 **Three fully playable casino games**
- 💰 **Shared credit system across games**
- 🧠 **Accurate rules & probability modeling**
- 🧱 **Modular file structure for each game**
- 🔁 **Game-level session loops with replay control**
- 🛡️ **Input validation and basic error handling**
- 🖥️ **Simple terminal-based interface**

---

## 💻 Installation & Usage

### Prerequisites
- Python 3.x installed on your machine

### Setup

```bash
git clone https://github.com/yourusername/pyarcade-casino.git
cd pyarcade-casino
```

### Run

```bash
python main.py
```

---

## 🕹️ Games Included

### ♠️ Blackjack

**Goal:** Beat the dealer by getting as close to 21 as possible without going over.  
**Rules:** Aces adjust between 1/11, Dealer hits until 17, Blackjack pays 2.5×

```text
================ BLACKJACK ================
Credits: 1000
Enter your bet : 100
Your hand: Q♦ K♦
Hand value: 20
Dealer shows: Q♥
------------------------------------------
Make choice (Hit/Stand): stand
...
============== RESULT ==============
You win! Payout: 200
Updated Credits: 1150
```

---

### 🎰 Slot Machine

**Goal:** Spin the reels and match symbols to win.

**Symbols Used**
```
['A', 'B', 'C', 'D', 'E', '⭐', '💎']
```

```text
========= SLOT MACHINE =========
Credits: 10000
Enter your bet : 1000
Spinning...
B | ⭐ | D

============= RESULT =============
Better luck next time!
Updated Credits: 9000
```

**Features**
- Probability-weighted symbol generation
- Realistic credit-based betting system
- Dynamic payout evaluation

---

### 🎯 Roulette

European-style wheel (0–36) with multiple betting options:

- Straight — Pick a number (35× payout)
- Color — Red / Black
- Even / Odd
- High / Low — Low (1–18), High (19–36)

```text
==========================================
             ROULETTE CASINO
==========================================
Credits: 10000
Allowed Bets: straight, color, even/odd, high/low

Choose the type of bet: color
Choose the value of bet(red or black): red
Enter the bet amount: 1000

Spinning the wheel...
Ball landed on : 30 RED

================= RESULT =================
Jackpot! You won 2000!
==========================================
Updated Credits: 11000
```

**Features**
- Multiple bet types
- Realistic wheel mechanics
- Payout evaluation system

---

## 🏗️ System Architecture

The project is organized into separate files, with each game implemented in its own module:

```
main.py      → Menu system and game selection  
slot.py      → Slot machine engine
black_jack.py → Blackjack engine
roulette.py  → Roulette engine
```
Credits are passed between functions to maintain state without using global variables.

## 🗂️ Project Structure

```text
PyArcade-Casino/
│
├── main.py          # Application entry point
├── slot.py          # Slot machine module
├── black_jack.py     # Blackjack module
├── roulette.py      # Roulette module
├── README.md        # Documentation
└── LICENSE          # MIT License
```

---

## 🧠 Learning Notes

Working on this project helped me understand:

- How quickly complexity grows as programs expand beyond a single file
- The importance of breaking logic into smaller, reusable functions
- How to manage shared state (credits) without relying on global variables
- Why refactoring repeated logic improves readability and maintainability
- How proper input validation improves overall program stability and user experience

---

## 🔧 Design Decisions

- Each game runs independently in its own module to keep logic isolated
- A central menu controls navigation and overall game flow
- Shared logic (such as input handling) is reused where possible to reduce duplication
- State is passed explicitly between functions to keep behavior predictable and easier to debug

---

## 🛣️ Possible Improvements

Some areas that could be improved or explored further:

- Refactoring parts of the code using classes (OOP approach)
- Adding automated tests for core game logic
- Improving code structure, naming consistency, and documentation
- Creating a basic GUI or web-based interface
- Expanding existing game logic or adding new games
---

## 📄 License

This project is licensed under the **MIT License**.
