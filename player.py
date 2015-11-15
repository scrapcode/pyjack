from hand import Hand

class Player:
    '''
    Represents a blackjack player that can have one or many hands.
    '''
    
    def __init__(self, name="Player", cash=100.00):
        self.name = name
        self.cash = cash
        self.hands = []
        
    def addHand(self, wager, isDealer=False):
        '''addHand(wager, isDealer)
        
        Adds a hand of cards to the Player's controlled hands of cards.
        
        Returns: None
        '''
        
        if wager > 0.0 or isDealer == True:
            newHand = Hand(wager)
            self.hands.append(newHand)