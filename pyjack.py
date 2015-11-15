"""PyJack

Blackjack in Python
"""

from game import Game
from player import Player

if __name__ == '__main__':
    
    # initialize a game of blackjack.
    blackjackGame = Game()
    
    # create a player.
    playerOne = Player("Player One")
    
    # add the player to the game.
    blackjackGame.addPlayer(playerOne)
    
    # create a hand with a $5.00 wager for the player to control.
    playerOne.addHand(5.00)
    
    # deal initial cards
    blackjackGame.dealInitialCards()
    
    # print game status
    blackjackGame.printGameStatus()