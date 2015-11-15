from player import Player

class Dealer:
    def __init__(self):
        self.player = Player("Dealer")
        self.hand = self.player.hands[0]
    
    