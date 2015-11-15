"""PyJack

Blackjack in Python
"""

from card import Card, Faces, Suits
from deck import Deck
from player import Player

if __name__ == '__main__':
    
    # Initiate a deck of cards, 3 decks in size.
    aDeck = Deck(3)
    
    # Shuffle the deck of cards.
    aDeck.shuffleDeck()
    
    # Create a Player with $100
    aPlayer = Player("Cameron", 100.00)
    
    # Add a hand worth $10 to that players hands
    aPlayer.addHand(10.00)

    # Deal player 2 cards.
    aPlayer.hands[0].addCard(aDeck.dealACard())
    aPlayer.hands[0].addCard(aDeck.dealACard())
    
    # Show hand
    print("{}'s current hand:".format(aPlayer.name))
    
    for card in aPlayer.hands[0].cards_in_hand:
        print("{} of {}: {}".format(card.face.name, card.suit.name, card.getValue()))
        
    print("Total value: {}".format(aPlayer.hands[0].total()))