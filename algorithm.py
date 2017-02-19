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
    pass

class Vegetable(object):
