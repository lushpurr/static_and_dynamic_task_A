import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setup(self):
        self.card = Card()
        self.card_game = CardGame(self.card)
    
    
