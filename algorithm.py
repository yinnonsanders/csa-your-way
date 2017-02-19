#algorithm for csa-your-way

class Box(object):
    """
    Attributes:
    User - User associated with box (Instance of User)
    Items - List of items in box (List of Vegetables)
    """
    def __init__(self, user, items):
        self.user = user
        self.items = []
    
    def add(self, item):
        """
        Precondition: item is of class vegetable
        """
        assert isinstance(item, Vegetable)
        
        self.items.append(item)

class User(object):
    
    def __init__(self, id, preferences, shares):
    """
    input id: int that points to costumer's id
    input preferences: list of 5 ints, 1 to 5, that correspond to user produce preferences
    input shares: int that equals the number of shares that user owns
    """
    
    

class Vegetable(object):

