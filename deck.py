from card import Card, Faces, Suits
from random import shuffle

class Deck:
    '''
    Represents and Deck of Cards
    '''
    cards_in_deck = []
    
    def __init__(self, deck_size=1):
        '''Deck(deck_size)
        
        Creates a deck of 52 cards in multiples of deck_size.
        '''
        for i in range(deck_size):
            for suit in Suits:
                for face in Faces:
                    newCard = Card(face, suit)
                    self.cards_in_deck.append(newCard)
                    
    def numberOfCardsInDeck(self):
        '''numberOfCardsInDeck()
        
        Returns the number of cards in the current Deck of Cards.
        
        Returns: integer
        '''
        return len(self.cards_in_deck)
        
    def shuffleDeck(self):
        '''shuffleDeck()
        
        Shuffles the Deck of Cards
        '''
        shuffle(self.cards_in_deck)
        
    def dealACard(self):
        '''dealACard()
        
        Removes a card from the deck and returns that Card.
        
        Returns: Card
        '''
        return self.cards_in_deck.pop()