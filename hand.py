from card import Card, Suits, Faces

class Hand:
    '''
    Represents a hand of cards.
    '''
    cards_in_hand = []
    bets_on_hand = 0.0
    
    def __init__(self, wager=0.0):
        self.bets_on_hand = wager
    
    def addCard(self, card):
        '''addCard(card)
        
        Adds a card to the Hand's available cards.
        '''
        self.cards_in_hand.append(card)
        
    def removeCard(self, card_to_remove):
        '''removeCard(card_to_remove)
        
        Removes an existing card from the Hand's available cards.
        '''
        for card in self.cards_in_hand:
            if card.face == card_to_remove.face and card.suit == card_to_remove.suit:
                del card
    
    def getNumberOfCards(self):
        '''getNumberOfCards()
        
        Returns an integer of the amount of cards in the Hand.
        
        Returns: integer
        '''
        return len(self.cards_in_hand)
        
    def containsAce(self):
        '''containsAce()
        
        Returns the number of Aces in the hand or False if there are none.
        '''
        totalAces = 0
        for card in self.cards_in_hand:
            if card.face == Faces.Ace:
                totalAces += 1
        return False
        
    def total(self):
        '''total()
        
        Returns the total score value of the Hand.
        '''
        total = 0
        for card in self.cards_in_hand:
            total += card.getValue()
        
        # If the hand contains multiple aces and the ace value of 11 causes the
        # hand to bust, the value of the aces should be lowered to 1 instead
        # until the hand is no longer a bust hand.
        if self.containsAce():
            for i in range(self.containsAce()):
                if total > 21:
                    total -= 10
        
        return total