import unittest
from DeckOfCards import Card, Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", 2)

    def test_init(self):
        """Each card should have both a suit and a value."""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, 2)

    def test_repr(self):
        """An instance representation should return a string in the format '{value} of {suit}'."""
        self.assertEqual(self.card.__repr__(), "2 of Hearts")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """Each deck should have a 'cards' attribute, which is a list consisting of 52 elements."""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """A deck representation should return a string in the format 'Deck of {number} cards'."""
        self.assertEqual(self.deck.__repr__(), "Deck of 52 cards.")

    def test_count(self):
        """Count method should return a number of cards currently in the deck."""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_error(self):
        """If no cards left in the deck, a value error is expected."""
        self.deck.cards.clear()
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_insufficient_cards(self):
        """If there are not enough cards left in the deck, '_deal' method should deal all remaining cards."""
        self.assertEqual(len(self.deck._deal(53)), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_sufficient_cards(self):
        """If there are enough cards in the deck, '_deal' method should deal the requested number of cards."""
        self.assertEqual(len(self.deck._deal(3)), 3)
        self.assertEqual(self.deck.count(), 49)

    def test_shuffle_not_full_deck(self):
        """A deck should be shuffled if it is full."""
        self.deck.deal_card()
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_shuffle_full_deck(self):
        """If a deck is not full, a value error should be thrown."""
        self.assertNotEqual(self.deck.cards, self.deck.shuffle())
        self.assertEqual(self.deck.count(), 52)

    def test_deal_card(self):
        """The 'deal_card' method should deal a single card from the deck."""
        self.assertEqual(self.deck.cards[-1], self.deck.deal_card())
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """The 'deal_hand' method should deal the number of cards passed as an argument."""
        self.assertEqual(len(self.deck.deal_hand(26)), 26)
        self.assertEqual(self.deck.count(), 26)

if __name__ == "__main__":
    unittest.main()































if __name__ == "__main__":
    unittest.main()


