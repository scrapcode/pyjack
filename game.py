from card import Card, Faces, Suits
from deck import Deck
from player import Player
from hand import HandStatus

class Game:
    def __init__(self, deck_size=6):
        self.min_bet = 5.00
        self.max_bet = 1000.00
        self.deck_size = deck_size
        self.deck = Deck(deck_size)
        self.deck.shuffleDeck()
        self.house_winnings = 0.00
        self.players = []
        self.dealer = Player("Dealer")
        self.dealer.addHand(0.00, True)
        
    def addPlayer(self, player):
        '''addPlayer(player)
        
        Adds a Player to the Game
        '''
        if player.cash >= self.min_bet:
            self.players.append(player)
        else:
            raise Exception("Player ({}) does not have enough cash to play at this game.".format(player.name))
    
    def dealInitialCards(self):
        '''dealInitialCards()
        
        Deals the initial 2 cards to each player.
        '''
        if self.deck.numberOfCardsInDeck() < 30:
            # when the shoe gets low, reshuffle a new deck.
            self.deck = Deck(self.deck_size)
            self.deck.shuffleDeck()
        
        if len(self.players) > 0:
            for i in range(2):
                for player in self.players:
                    current_hand = 1
                    for hand in player.hands:
                        # add a card to each hand/
                        cardToAdd = self.deck.dealACard()
                        hand.addCard(cardToAdd)
                        current_hand += 1
                        
                            
                # deal to the dealer last
                dealerCardToAdd = self.deck.dealACard()
                self.dealer.hands[0].addCard(dealerCardToAdd)
            
            # check for blackjacks
            for player in self.players:
                for hand in player.hands:
                    if hand.total() == 21:
                        # blackjack!
                        hand.status = HandStatus.Blackjack
                    elif hand.total() > 21:
                        # bust
                        hand.status = HandStatus.Bust
                    else:
                        hand.status = HandStatus.Open
        else:
            raise Exception("There are no players at the game.")
            
    def isInsuranceOpportunity(self):
        '''
        If the dealer has 2 cards and the second is an Ace, then there is an
        insurance opportunity.
        '''
        if len(self.dealer.hands) > 0:
            if self.dealer.hands[0].getNumberOfCards() > 1:
                if self.dealer.hands[0].cards_in_hand[1].face == Faces.Ace:
                    return True
        return False

    def printGameStatus(self):
        '''
        Prints the game status to the console.
        '''
        print("{} players at the table.".format(len(self.players)))
        
        print("Dealers hand:")
        for card in self.dealer.hands[0].cards_in_hand:
            print("{} of {}".format(card.face.name, card.suit.name))
            
        print("Dealers total: {}\n\n".format(self.dealer.hands[0].total()))
            
        for player in self.players:
            current_hand = 1
            for hand in player.hands:
                print("{}'s hand #{}:".format(player.name, current_hand))
                
                for card in hand.cards_in_hand:
                    print("{} of {}".format(card.face.name, card.suit.name))
                    
                print("Hand #{} Total: {}\n\n".format(current_hand, hand.total()))
                current_hand += 1
                
    def currentNumberOfHands(self):
        n = 0
        for player in self.players:
            n += len(player.hands)
        return n