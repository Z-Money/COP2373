import functools


def gatherExpenses():
    """
    Gathers a list of all user expenses.

    Parameters:
        None

    Variables:
        expenses (list): A list of all user expenses.
        expenseType (str): The expense type.
        amount (int): The expense amount.
        more (str): Determines if the user has additional expenses to record.

    Logic:
        1. Receive an expense type from the user.
        2. Receive an expense amount from the user.
        3. Try to convert the expense amount to a float.
        4. Append the expense type and amount to the list of expenses.
        5. Prompt the user if they have additional expenses to record.
        6. Return the list of expenses.

    Returns:
        list: A list of all user expenses.
    """
    # Initialize list of expenses
    expenses = []

    # Take expense inputs until user is finished
    while True:
        # Take initial inputs from user for expense type and amounts
        expenseType = input("Enter expense type: ")
        amount = input("Enter expense amount: ")

        # Convert the expense amount for arithmic calculations
        try:
            amount = float(amount)

        # Account for user input errors when inputting expense amount
        except ValueError:
            print("Invalid expense amount")
            continue

        # Add expenses type and amount as dictionary to list of expenses
        expenses.append({"type": expenseType, "amount": amount})

        # Prompt user to add additional expenses, break loop if no
        more = input("Add another expense? (y/n): ")
        if more.lower() != "y":
            break

    # Return list of expenses
    return expenses


def analyzeExpenses(expenses):
    """
    Analyzes a list of expenses to find the total, highest, and lowest values.

    Parameters:
        expenses (list): A list of all user expenses.

    Variables:
        total (int): The total expense amount.
        highest (dict): A dictionary of highest expense type and amount.
        lowest (dict): A dictionary of lowest expense type and amount.

    Logic:
        1. Calculates the total expense amount.
        2. Calculates the highest expense type and amount.
        3. Calculates the lowest expense type and amount.
        4. Prints the values of the total, highest, and lowest expenses.

    Returns:
        None
    """
    # Calculate sum of all expenses
    getTotal = lambda acc, x: acc + x["amount"]
    total = functools.reduce(getTotal, expenses, 0)

    # Calculate the highest expense by comparing all values
    getHighest = lambda acc, x: x if x["amount"] > acc["amount"] else acc
    highest = functools.reduce(getHighest, expenses)

    # Calculate the lowest expense by comparing all values
    getLowest = lambda acc, x: x if x["amount"] < acc["amount"] else acc
    lowest = functools.reduce(getLowest, expenses)

    # Print the total, highest, and lowest expenses, rounding to 2 decimals
    print(f"\nTotal expenses: ${total:.2f}")
    print(f"Highest expense: {highest['type']} - ${highest['amount']:.2f}")
    print(f"Lowest expense: {lowest['type']} - ${lowest['amount']:.2f}")


if __name__ == "__main__":
    inputtedExpenses = gatherExpenses()
    analyzeExpenses(inputtedExpenses)
