class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Your current balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("No sufficient balance")
        else:
            self.balance -= amount
            print(f"Your current balance is {self.balance}")
    
    def check_balance(self):
        print(f"Your current balance is {self.balance}")


account_number = input("Enter account number: ")
account = BankAccount(account_number)

while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = input("Enter amount to withdraw: ")
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
        
            break
        else:
            print("kandam vazhi oduka! Please try again.")



