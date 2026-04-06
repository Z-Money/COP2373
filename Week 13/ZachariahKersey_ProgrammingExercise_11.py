import random

class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card   = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...!!!")
        self.current_card += 1
        return self.card_list[self.current_card - 1]

def display_hand(hand):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    for card in hand:
        r = card % 13
        s = card // 13
        print(f"{ranks[r]} of {suits[s]}")

def main():
    myDeck = Deck(52)

    hand = []
    for i in range(5):
        hand.append(myDeck.deal())

    print("Your hand:")
    display_hand(hand)

    numbers = input("Enter a list of numbers separated by a comma: ")
    numbers = numbers.replace(" ", "").split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    for i in numbers:
        if 1 <= i <= 5:
            hand[i - 1] = myDeck.deal()

    print("\nYour new hand:")
    display_hand(hand)

if __name__ == "__main__":
    main()