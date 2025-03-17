import unittest
from blackjack import Card, Deck, Hand

class TestBlackjack(unittest.TestCase):

    def test_card_creation(self):
        card = Card("Hearts", "A")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "A")
        self.assertEqual(card.value, 11)

    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertTrue(all(isinstance(card, Card) for card in deck.cards))

    def test_deck_shuffling(self):
        deck1 = Deck()
        deck2 = Deck()
        self.assertNotEqual([card.rank for card in deck1.cards], [card.rank for card in deck2.cards])

    def test_hand_add_card(self):
        hand = Hand()
        card = Card("Spades", "K")
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.value, 10)

    def test_hand_value_with_ace(self):
        hand = Hand()
        hand.add_card(Card("Hearts", "A"))
        hand.add_card(Card("Spades", "K"))
        self.assertEqual(hand.value, 21)

    def test_hand_value_with_ace_adjustment(self):
        hand = Hand()
        hand.add_card(Card("Hearts", "A"))
        hand.add_card(Card("Spades", "K"))
        hand.add_card(Card("Diamonds", "8"))
        self.assertEqual(hand.value, 19)  # Ace should adjust to value 1

    def test_bust_hand(self):
        hand = Hand()
        hand.add_card(Card("Hearts", "A"))
        hand.add_card(Card("Spades", "K"))
        hand.add_card(Card("Diamonds", "Q"))
        hand.add_card(Card("Clubs", "10"))
        self.assertTrue(hand.value > 21)

if __name__ == "__main__":
    unittest.main()
