import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setup(self):
        self.card = Card()
        self.card_game = CardGame(self.card)
    
    def test_check_for_ace_true(self):
        card1 = Card("hearts", 1)
        result = CardGame.check_for_ace(self, card1)
        self.assertEqual(True, result)

    def test_check_for_ace_false(self):
        card1 = Card("hearts", 2)
        result = CardGame.check_for_ace(self, card1)
        self.assertEqual(False, result)

    def test_highest_card_card1(self):
        card1 = Card("hearts", 10)
        card2 = Card("spades", 2)
        result = CardGame.highest_card(self, card1, card2)
        self.assertEqual(card1, result)
        

    def test_highest_card_card2(self):
        card1 = Card("hearts", 2)
        card2 = Card("spades", 10)
        result = CardGame.highest_card(self, card1, card2)
        self.assertEqual(card2, result)

    def test_cards_total(self):
        card1 = Card("hearts", 2)
        card2 = Card("spades", 10)
        card3 = Card("diamonds", 5)
        cards = [card1, card2, card3]
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 17", result)
        

    