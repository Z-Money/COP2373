def validatePurchase(totalTickets, ticketsPurchased):
    """
    Validates that the requested amount of tickets is valid.

    Parameters:
        totalTickets (str): The total number of tickets available for sale
        ticketsPurchased (int): The number of tickets requested for purchase

    Variables:
        totalTickets (int): The total number of tickets available for sale

    Logic:
        1. Convert ticketsPurchased to an integer.
        2. Check if ticketsPurchased is a positive integer.
        3. Check if ticketsPurchased is below 4-ticket limit.
        4. Check if there are enough tickets to sell the requested amount.
        5. Return True to indicate that we can buy the tickets.

    Returns:
        True or False.
    """
    # Convert ticketsPurchased to an integer
    try:
        ticketsPurchased = int(ticketsPurchased)
    # Handle potential errors due to type mismatch
    except ValueError:
        print("Please enter an integer")
        return False
    # Runs only if the conversion above runs without error
    else:
        # Prevent any negative number of tickets from being purchased
        if ticketsPurchased < 1:
            print("Please enter a positive integer")
            return False
        # Enforces the limit of 4 tickets from being purchased
        if ticketsPurchased > 4:
            print("Sorry, you cannot buy more than 4 tickets")
            return False
        # Ensures that there are enough tickets left to be bought
        if ticketsPurchased > totalTickets:
            print("We don't have that many tickets")
            return False
        # Returns that the input is valid if it passes all the above test
        return True

def processOrder():
    """
    Handles the process of selling tickets purchased.

    Parameters:
        None

    Variables:
        tickets (int): The total number of tickets available for sale
        buyers (int): The number of buyers
        ticketsPurchased (int): The number of tickets requested for purchase

    Logic:
        1. Initialize tickets for sale and number of buyers.
        2. Print the number of tickets available for purchase upon first run.
        3. Loop through prompting for purchasing tickets until none are left.
        4. Prompt for a number of tickets to purchase.
        5. Validate the request number of tickets across various criteria.
        6. Update the number of tickets remaining.
        7. Increase the numbers of buyers by 1.
        8. Print the new number of tickets remaining.
        9. Upon no tickets remaining, print the total number of buyers.

    Return:
        None
    """
    # Initialize the tickets available for purchase and the number of buyers
    tickets = 10
    buyers = 0
    # Print the number of tickets remaining prior to the first run of the loop
    print("Tickets remaining: " + str(tickets))
    # Repeat prompting for the purchase of tickets until none are left for sale
    while tickets > 0:
        ticketsPurchased = input("How many tickets would you like: ")
        # Update the number of tickets and buyers if ticketsPurchased is valid
        if validatePurchase(tickets, ticketsPurchased):
            tickets = tickets - int(ticketsPurchased)
            buyers += 1
            print("Tickets remaining: " + str(tickets) + "\n")
        # Prints the number of tickets remaining if ticketsPurchased is invalid
        else:
            print("Tickets remaining: " + str(tickets) + "\n")
    # Prints the number of total buyers once no tickets are left for sale
    print("Total buyers: " + str(buyers))

# Runs main function if this file is being run directly
if __name__ == '__main__':
    # Start processing any orders for tickets
    processOrder()