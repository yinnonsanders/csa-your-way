#algorithm for csa-your-way
from vegetables import *

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
    

    def get_box(self, yieldDict):
        """returns a box object based on preferences and yield
        input yieldDict: Dictionary that tells the weekly yield
        """
        prices = get_scaled_prices(vegetablePrices)
        for vegetable in vegetableList:
             
        
    def get_scaled_prices(vegetablePrices):    
        pass

    
def get_distribution(userList, yieldDict):

    """returns a list of boxes
    yieldDict: weekly produce yield
    userList" list of users
    """
    boxList = []
    for user in userList:
        boxList.append(user.get_box(yieldDict))
    return boxList
    
    
    
    