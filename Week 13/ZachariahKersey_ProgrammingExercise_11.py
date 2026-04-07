# Import random module to shuffle list
import random

# Initialize class to create a deck of cards
class Deck:
    # Define an initialization method, including all variables
    def __init__(self, size):
        # Create a card list with all numbers between 0 and the deck size
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size
    # Method for dealing cards
    def deal(self):
        # Reset and shuffle the deck if there are no more cards in the deck
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...!!!")
        self.current_card += 1
        # Return the next card in the deck
        return self.card_list[self.current_card - 1]

# Function to display the user's hand
def display_hand(hand):
    # Define the possible ranks and suits for the cards
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    # Iterate over every card in the user's hand, printing its rank and suit
    for i in range(len(hand)):
        card = hand[i]
        r = card % 13
        s = card // 13
        print(f"{i + 1}: {ranks[r]} of {suits[s]}")

# Function to get the cards to replace
def gather_cards_to_replace():
    # Continue asking for a series of numbers until they are valid
    while True:
        # Gather the series of numbers, remove spaces, and separating by commas
        numbers = input("Enter a series of numbers to be replaced (Ex: 1, 3, 5): ")
        numbers = numbers.replace(" ", "").split(",")

        # Try/except block to catch any noninteger values
        try:
            numbers = list(map(int, numbers))
        except ValueError:
            print("Please enter valid integers.")
            continue

        # Test for any values not within the valid option choices
        for num in numbers:
            if num < 1 or num > 5:
                print("Please enter a valid option.")
                break

        # Return the inputted numbers upon for-loop completion
        else:
            return numbers

# Function to handle the main processes of the program
def main():
    # Create a standard deck of cards
    myDeck = Deck(52)

    # Create an empty hand for the user, then deal 5 cards to them
    hand = []
    for i in range(5):
        hand.append(myDeck.deal())

    # Display the user's hand
    print("Your hand:")
    display_hand(hand)

    # Gather the cards to be replaced, handling input errors
    numbers = gather_cards_to_replace()

    # Iterate over all chosen cards to replace them
    for i in numbers:
        hand[i - 1] = myDeck.deal()

    # Print new hand to the user
    print("\nYour new hand:")
    display_hand(hand)

if __name__ == "__main__":
    main()