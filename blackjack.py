import random

# Define the card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.ace = True

    def adjust_for_ace(self):
        if self.value > 21 and self.ace:
            self.value -= 10
            self.ace = False

# Game class
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def show_hands(self, show_dealer_card=False):
        print("\nPlayer's Hand:")
        for card in self.player_hand.cards:
            print(card)
        print(f"Value: {self.player_hand.value}")

        print("\nDealer's Hand:")
        if show_dealer_card:
            for card in self.dealer_hand.cards:
                print(card)
            print(f"Value: {self.dealer_hand.value}")
        else:
            print(f"{self.dealer_hand.cards[0]} and Hidden Card")

    def player_turn(self):
        while True:
            choice = input("\nDo you want to (h)it or (s)tand? ").lower()
            if choice == 'h':
                self.player_hand.add_card(self.deck.deal())
                self.player_hand.adjust_for_ace()
                print(f"\nPlayer drew: {self.player_hand.cards[-1]}")
                print(f"Value: {self.player_hand.value}")
                if self.player_hand.value > 21:
                    print("You bust! Dealer wins.")
                    return False
            elif choice == 's':
                break
            else:
                print("Invalid input. Please choose (h)it or (s)tand.")
        return True

    def dealer_turn(self):
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.adjust_for_ace()
            print(f"\nDealer drew: {self.dealer_hand.cards[-1]}")
            print(f"Value: {self.dealer_hand.value}")
            if self.dealer_hand.value > 21:
                print("Dealer busts! You win!")
                return False
        return True

    def check_winner(self):
        if self.player_hand.value > 21:
            print("\nYou bust! Dealer wins.")
        elif self.dealer_hand.value > 21:
            print("\nDealer busts! You win!")
        elif self.player_hand.value > self.dealer_hand.value:
            print("\nYou win!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("\nDealer wins!")
        else:
            print("\nIt's a tie!")

# Main function to play the game
def play_game():
    game = BlackjackGame()
    game.deal_cards()
    game.show_hands()

    if not game.player_turn():
        return

    if not game.dealer_turn():
        return

    game.show_hands(show_dealer_card=True)
    game.check_winner()

# Run the game
if __name__ == "__main__":
    play_game()
