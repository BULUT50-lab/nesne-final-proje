class Account:
    accounts = []  # Static list to hold all account objects

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        Account.accounts.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")
            Bank.track_transaction(f"Deposited {amount} to account {self.account_number}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
                Bank.track_transaction(f"Withdrew {amount} from account {self.account_number}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def view_balance(self):
        print(f"Account Owner: {self.owner}\nAccount Number: {self.account_number}\nBalance: {self.balance}")

class Bank:
    transaction_history = []  # Static list to hold transaction history

    @staticmethod
    def display_bank_info():
        print("Welcome to the Bank Management System!")
        print(f"Total Accounts: {len(Account.accounts)}")

    @staticmethod
    def track_transaction(description):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Bank.transaction_history.append(f"{timestamp} - {description}")

    @staticmethod
    def view_transaction_history():
        print("Transaction History:")
        for transaction in Bank.transaction_history:
            print(transaction)

# Example usage (comment out or remove this section in production):
if __name__ == "__main__":
    acc1 = Account("12345", "Alice", 1000.0)
    acc2 = Account("67890", "Bob", 500.0)

    acc1.deposit(200)
    acc1.withdraw(500)
    acc1.view_balance()

    acc2.deposit(100)
    acc2.withdraw(700)
    acc2.view_balance()

    Bank.display_bank_info()
    Bank.view_transaction_history()
