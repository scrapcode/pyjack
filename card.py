from enum import Enum

################################
# Enums
#
class Faces(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

class Suits(Enum):
    Spades = 1
    Clubs = 2
    Diamonds = 3
    Hearts = 4
#
# /Enums
################################
    
class Card:
    def __init__(self, face=None, suit=None):
        self.face = face
        self.suit = suit
        
    def getValue(self):
        '''getValue()
        
        Returns the value of the Card
        
        Returns: integer
        '''
        if self.face == None:
            return 0
        elif self.face == Faces.Ace:
            return 11
        elif self.face == Faces.Jack or self.face == Faces.Queen or self.face == Faces.King:
            return 10
        else:
            return self.face.value