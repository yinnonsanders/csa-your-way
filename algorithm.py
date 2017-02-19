#algorithm for csa-your-way

class Box(object):
    """
    Attributes:
    Items - Dictionary of items in box and amount ()
    """
    def __init__(self, items):
        self.items = {}
    
    def add(self, vegetable, amount):
        """
        Precondition: vegetable is a valid vegetable
        amount is an int or float.
        """
        
        self.items[vegetable] = amount

class User(object):
    
    def __init__(self, id, preferences, shares):
    """
    input id: int that points to costumer's id
    input preferences: list of 5 ints, 1 to 5, that correspond to user produce preferences
    input shares: int that equals the number of shares that user owns
    """
