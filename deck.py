from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return "Deck of {} cards.".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self,num):
        cards_left = self.count()
        actual_num = min([cards_left, num])
        if cards_left == 0:
            raise ValueError("All cards have been dealt.")
        dealt_cards = self.cards[-actual_num:]
        self.cards = self.cards[:-actual_num]
        return dealt_cards

    def shuffle(self):

        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)

