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
        self.AssertEqual(True, result)

    