class BankAcct:
    def __init__(self, name, acct_num, balance, interest_rate, interest):
        self.name = name
        self.acct_num = acct_num
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = interest

    def adjust_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def manage_balance(self, amount, operation):
        if operation == "withdraw":
            self.balance -= amount
        elif operation == "deposit":
            self.balance += amount

    def get_balance(self):
        return f"Account Balance: ${self.balance}"

    def calculate_interest(self, days):
        interest = self.balance * self.interest_rate * days
        self.balance += interest
        self.interest += interest
        return f"Calculated Interest: ${interest:.2f}"

    def __str__(self):
        return (f"Balance: ${self.balance:.2f}\nInterest Rate: "
                f"{self.interest_rate*100:.2f}%\n"
                f"Total Interest: ${self.interest:.2f}")

def test():
    bankAcct = BankAcct("Bank Account", 1, 500.00, 0.01, 0)
    print("Initial Bank Account Details:")
    print(bankAcct)

    bankAcct.manage_balance(100, operation="withdraw")
    print("\nAfter Withdraw:")
    print(bankAcct)

    bankAcct.manage_balance(300, operation="deposit")
    print("\nAfter Deposit:")
    print(bankAcct)

    print("\nCalculating Interest:")
    print(f"{bankAcct.calculate_interest(2)}")
    print(bankAcct)

    print("\nBank Account Balance:")
    print(bankAcct.get_balance())
    print(bankAcct)

    bankAcct.adjust_interest_rate(.5)
    print("\nAdjusting Interest Rate:")
    print(bankAcct)

if __name__ == "__main__":
    test()