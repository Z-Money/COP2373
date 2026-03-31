# Initialize class to manage Bank Accounts
class BankAcct:
    # Define an initialization method, including all variables
    def __init__(self, name, acct_num, balance, interest_rate, interest):
        self.name = name
        self.acct_num = acct_num
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = interest
    # Method for adjusting the interest rate for the bank account
    def adjust_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
    # Method for managing the balance of the account
    def manage_balance(self, amount, operation):
        # Subtract amount from balance if withdrawing from account
        if operation == "withdraw":
            self.balance -= amount
        # Add amount to balance if depositing into account
        elif operation == "deposit":
            self.balance += amount
        # Handle potential issues with invalid operations
        else:
            print("\nError with managing account balance. "
                  "Operation must be either 'withdraw' or 'deposit'")
    # Method for accessing the balance of the account
    def get_balance(self):
        return self.balance
    # Method for calculating interest over a number of days
    def calculate_interest(self, days):
        # Calculate the interest in the account based on the number of days
        interest = self.balance * self.interest_rate * days
        # Add the interest to the account and the total interest amount
        self.balance += interest
        self.interest += interest
        # Return the calculated interest
        return f"Calculated Interest: ${interest:.2f}"
    # Overriding string method of BankAcct class
    def __str__(self):
        # Return a string with all the bank details
        return (f"{self.name} (#{self.acct_num})\n"
                f"Balance: ${self.balance:.2f}\nInterest Rate: "
                f"{self.interest_rate*100:.2f}%\n"
                f"Total Interest: ${self.interest:.2f}")

# Create a test function to show the different methods of the BankAcct class
def test():
    # Create bankAcct object
    bankAcct = BankAcct("Zachariah's Bank Account", 1, 500.00, 0.01, 0)

    # Print the initial details of the bank account
    print("Initial Bank Account Details:")
    print(bankAcct)

    # Perform the withdrawal method and print the new account details
    bankAcct.manage_balance(100, operation="withdraw")
    print("\nAfter Withdraw:")
    print(bankAcct)

    # Perform the deposit method and print the new account details
    bankAcct.manage_balance(300, operation="deposit")
    print("\nAfter Deposit:")
    print(bankAcct)

    # Calculate the interest and print the new account details
    print("\nCalculating Interest:")
    print(f"{bankAcct.calculate_interest(2)}")
    print(bankAcct)

    # Access only the bank account balance
    print("\nBank Account Balance:")
    print(f"Account Balance: ${bankAcct.get_balance()}")

    # Adjust the interest rate and print the new account details
    bankAcct.adjust_interest_rate(.5)
    print("\nAdjusting Interest Rate:")
    print(bankAcct)

if __name__ == "__main__":
    # Run the test function to show the methods of the BankAcct class
    test()