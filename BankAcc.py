class BankAcc:
    def __init__(self):
        self.acc_holder_name = input("Enter account holder name: ")
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.acc_holder_name}")
        print(f"Balance: {self.balance}")


acc = BankAcc()
acc.display_balance()
acc.deposit(150)
acc.withdraw(200)
acc.display_balance()
