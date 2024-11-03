# Simple Bank System with User Authentication
users = {
    "jmax1": {"password": "password123", "balance": 1000.0},
    "jmax2": {"password": "securepass", "balance": 1500.0}
}

# Function to validate username and password
def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return True
    else:
        return False

# Function to deposit money
def deposit(username, amount):
    if amount > 0:
        users[username]["balance"] += amount
        print(f"Deposit successful! Your new balance is: ${users[username]['balance']:.2f}")
    else:
        print("Invalid deposit amount.")

# Function to withdraw money
def withdraw(username, amount):
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > users[username]["balance"]:
        print("Insufficient funds.")
    else:
        users[username]["balance"] -= amount
        print(f"Withdrawal successful! Your new balance is: ${users[username]['balance']:.2f}")

# Function to view balance
def view_balance(username):
    print(f"Your current balance is: ${users[username]['balance']:.2f}")

# Main program
print("Welcome to the Simple Bank System")

username = input("Enter your username: ")
password = input("Enter your password: ")

# Authentication
if authenticate(username, password):
    print("Login successful!")
    while True:
        print("\nPlease select an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            deposit(username, amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            withdraw(username, amount)

        elif choice == "3":
            view_balance(username)

        elif choice == "4":
            print("Thank you for using the Simple Bank System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
else:
    print("Invalid username or password.")
