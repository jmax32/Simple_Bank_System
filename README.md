# Simple Bank System

A command-line based **Banking System** built with Python that allows users to securely deposit, withdraw, and view their account balance. This project is designed to illustrate basic banking operations with a simple user authentication mechanism.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Project Overview

The **Simple Bank System** provides an easy-to-use, text-based interface where users can manage their bank accounts. Users authenticate with a username and password, allowing them access to check their balance, deposit money, or withdraw funds. This project demonstrates foundational banking concepts and can serve as a base for more complex banking applications.

---

## Features

1. **User Authentication**:
   - Ensures users can securely log in to their accounts with a username and password.
   
2. **Deposit**:
   - Users can deposit money into their account, which increases their balance.

3. **Withdrawal**:
   - Users can withdraw money, provided they have sufficient balance.

4. **Balance Inquiry**:
   - Users can view their current account balance at any time after logging in.

5. **Command-Line Interface**:
   - Simple text-based user interface for easy command-line interaction.

---

## Technologies Used

- **Python**: Core programming language for developing the application.

---

## Installation

### Prerequisites
- Python 3 installed on your machine.

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-bank-system.git
   cd simple-bank-system
   ```

2. Run the application:
   ```
   python bank_system.py
   ```

---

## Usage

1. Run the program.
2. Enter your username and password to authenticate.
3. Choose from the following options:
   - **Deposit Money**: Enter the amount to deposit, which will add to your balance.
   - **Withdraw Money**: Enter the amount to withdraw. Withdrawal is permitted if the account balance is sufficient.
   - **View Balance**: Displays the current balance.
   - **Exit**: Log out of the system.

---

## Project Structure

- **bank_system.py**: Main program file containing user authentication, deposit, withdrawal, and balance-checking functions.
- **users**: Hardcoded user data simulating a basic database, with fields like `username`, `password`, and `balance`.

---

## Future Enhancements

1. **User Registration**:
   - Allow users to register new accounts with a username and password.

2. **Data Persistence**:
   - Store user data in a database or text file for persistence.

3. **Improved Security**:
   - Secure password handling with hashing for better security.

4. **Transaction History**:
   - Log each transaction, allowing users to view their transaction history.

5. **Enhanced UI**:
   - Develop a graphical user interface (GUI) for a more intuitive user experience.

---
