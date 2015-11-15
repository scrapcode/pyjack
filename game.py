from card import Card, Faces, Suits
from deck import Deck
from player import Player

class Game:
    def __init__(self, deck_size=6):
        self.dealer = Player("Dealer")
        self.min_bet = 5.00
        self.max_bet = 1000.00
        self.deck = Deck(deck_size)
        self.deck.shuffleDeck()
        self.house_winnings = 0.00
        self.players = []
        
    def addPlayer(self, player):
        '''addPlayer(player)
        
        Adds a Player to the Game
        '''
        if player.cash >= self.min_bet:
            self.players.append(player)
        else:
            raise Exception("Player ({}) does not have enough cash to play at this game.".format(player.name))
            