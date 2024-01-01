class BankAccount:

    def __init__(self, account_number, account_holder_name, account_type, balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def display_details(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance}")

    def display_balance(self):
        print(f"Balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
            self.display_details()
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            self.display_details()
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            self.display_balance()

account1 = BankAccount(account_number="20040156498523", account_holder_name="Ashwin_dileep", account_type="Savings", balance=10045621.0)

while True:
    print("\n1. Display Account Details")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        account1.display_details()
    elif choice == '2':
        deposit_amount = float(input("Enter the deposit amount: "))
        account1.deposit(deposit_amount)
    elif choice == '3':
        withdraw_amount = float(input("Enter the withdrawal amount: "))
        account1.withdraw(withdraw_amount)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

