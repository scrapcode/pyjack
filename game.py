from card import Card, Faces, Suits
from deck import Deck
from player import Player

class Game:
    def __init__(self, deck_size=6):
        self.min_bet = 5.00
        self.max_bet = 1000.00
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
        if len(self.players) > 0:
            for i in range(2):
                for player in self.players:
                    current_hand = 1
                    for hand in player.hands:
                        # add a card to each hand/
                        cardToAdd = self.deck.dealACard()
                        hand.addCard(cardToAdd)
                        
                        # DEBUG
                        print("Added {} of {} to {}'s hand #{}".format(cardToAdd.face.name, cardToAdd.suit.name, player.name, current_hand))
                        current_hand += 1
                        
                # deal to the dealer last/
                dealerCardToAdd = self.deck.dealACard()
                self.dealer.hands[0].addCard(dealerCardToAdd)
                # DEBUG
                print("Added {} of {} to {}'s hand.".format(dealerCardToAdd.face.name, dealerCardToAdd.suit.name, self.dealer.name))
        else:
            raise Exception("There are no players at the game.")
            
    def printGameStatus(self):
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