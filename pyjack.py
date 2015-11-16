"""PyJack

Blackjack in Python
"""
import os
from game import Game
from player import Player
from texttable import Texttable
from hand import HandStatus

def drawTable(game, showDealersCards=False):
    atmp = os.system('clear')
    
    table = Texttable()
    
    header = []
    row_wager = []
    row_cards = []
    row_totals = []
    row_status = []
    
    #
    # Add dealer's hand
    #
    header.append("Dealer")
    row_wager.append("")
    
    if showDealersCards:
        dealersCards = "{} of {}\n{} of {}".format(game.dealer.hands[0].cards_in_hand[0].face.name, game.dealer.hands[0].cards_in_hand[0].suit.name, game.dealer.hands[0].cards_in_hand[1].face.name, game.dealer.hands[0].cards_in_hand[1].suit.name)
        dealersTotal = game.dealer.hands[0].total()
    else:
        dealersCards = "X\n{} of {}".format(game.dealer.hands[0].cards_in_hand[1].face.name, game.dealer.hands[0].cards_in_hand[1].suit.name)
        dealersTotal = ""
    
    row_cards.append(dealersCards)
    row_totals.append(dealersTotal)
    row_status.append("")
    #
    # /dealer
    #
    
    for player in game.players:
        for hand in player.hands:
            header.append(player.name)
            row_wager.append("Bet: $" + str(hand.wager))
            row_cards.append("{} of {}\n{} of {}".format(hand.cards_in_hand[0].face.name, hand.cards_in_hand[0].suit.name, hand.cards_in_hand[1].face.name, hand.cards_in_hand[1].suit.name))
            row_totals.append("Total: {}".format(hand.total()))
            
            if hand.status == HandStatus.Blackjack:
                handStatus = "Blackjack!!"
            elif hand.status == HandStatus.Bust:
                handStatus = "Bust"
            else:
                handStatus = ""
                
            row_status.append(handStatus)
            
    table.header(header)
    table.add_row(row_wager)
    table.add_row(row_cards)
    table.add_row(row_totals)
    table.add_row(row_status)
    
    table.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.VLINES)
    
    print(table.draw())

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
    
    # DEBUG print game status
    #blackjackGame.printGameStatus()
    
    if blackjackGame.isInsuranceOpportunity():
        # ask for insurance if the dealer has an ace showing
        print("Dealer: is anyone interested in insurance? Y/N")
        
    drawTable(blackjackGame)