from hand import Hand

class Player:
    '''
    Represents a blackjack player that can have one or many hands.
    '''
    
    # List of hands currently controlled by the player.
    hands = []
    
    def __init__(self, name="Player", cash=100.00):
        self.name = name
        self.cash = cash
        
    def addHand(self, wager):
        '''addHand(wager)
        
        Adds a hand of cards to the Player's controlled hands of cards.
        
        Returns: None
        '''
        
        if wager > 0.0:
            newHand = Hand(wager)
            self.hands.append(newHand)