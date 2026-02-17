import functools


def gatherExpenses():
    # Initialize list of expenses
    expenses = []

    # Take expense inputs until user is finished
    while True:
        expenseType = input("Enter expense type: ")
        amount = input("Enter expense amount: ")

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid expense amount")
            continue

        expenses.append({"type": expenseType, "amount": amount})

        more = input("Add another expense? (y/n): ")
        if more.lower() != "y":
            break

    return expenses


def analyzeExpenses(expenses):
    # Calculate sum of all expenses
    getTotal = lambda acc, x: acc + x["amount"]
    total = functools.reduce(getTotal, expenses, 0)

    # Highest
    getHighest = lambda acc, x: x if x["amount"] > acc["amount"] else acc
    highest = functools.reduce(getHighest, expenses)

    # Lowest
    getLowest = lambda acc, x: x if x["amount"] < acc["amount"] else acc
    lowest = functools.reduce(getLowest, expenses)

    print(f"\nTotal expenses: ${total:.2f}")
    print(f"Highest expense: {highest['type']} - ${highest['amount']:.2f}")
    print(f"Lowest expense: {lowest['type']} - ${lowest['amount']:.2f}")


if __name__ == "__main__":
    inputtedExpenses = gatherExpenses()
    analyzeExpenses(inputtedExpenses)
