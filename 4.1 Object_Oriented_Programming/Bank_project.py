class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than 0."
        
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return "Deposit successful."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than 0."
        
        if amount > self.balance:
            return "Insufficient funds."
        
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        return "Withdrawal successful."

    def check_balance(self):
        return f"Current balance: {self.balance:.2f}"

    def show_transactions(self):
        if not self.transactions:
            return "No transactions yet."
        return "\n".join(self.transactions)


# -------- CLI PROGRAM --------

def display_menu():
    print("\n========== BANK MENU ==========")
    print("1 → Deposit")
    print("2 → Withdraw")
    print("3 → Check Balance")
    print("4 → Transaction History")
    print("5 → Exit")
    print("================================")


# Ask user for starting balance
while True:
    try:
        starting_balance = float(input("Enter starting balance: "))
        if starting_balance < 0:
            print("Balance cannot be negative.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

account = BankAccount(starting_balance)

print("\nWelcome to Your Bank Account System!")

running = True

while running:
    display_menu()
    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        try:
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "3":
        print(account.check_balance())

    elif choice == "4":
        print("\n--- Transaction History ---")
        print(account.show_transactions())

    elif choice == "5":
        print("\nThank you for banking with us. Goodbye!")
        running = False

    else:
        print("Invalid choice. Please select between 1 and 5.")

    if running:
        input("\nPress Enter to continue...")