#algorithm for csa-your-way
import vegetables

class Box(object):
    """
    Attributes:
    Userid - Id of user associated with this box (int)
    Items - Dictionary of items in box and amount (dict)
    """
    def __init__(self, userid):
        self.userid = userid
        self.items = {}
    
    def add(self, vegetable, amount):
        """
        Precondition: vegetable is a valid vegetable
        amount is an int or float.
        """
        
        self.items[vegetable] = amount

class User(object):
    
    def __init__(self, id, preferences, shares, box):
    """
    input id: int that points to costumer's id
    input preferences: dictionary that correspond to user produce preferences, 0 to 10
    input shares: int that equals the number of shares that user owns
    """
