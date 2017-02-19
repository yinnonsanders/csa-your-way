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
    
    def __init__(self, id, preferences, shares):
        """
        input id: int that points to costumer's id
        input preferences: dictionary that correspond to user produce preferences, 0 to 10
        input shares: int that equals the number of shares that user owns
        """
        
        self.id = id
        self.preferences = preferences
        self.shares = shares

    def get_box(self, yieldDict, totalPreferences):
        """returns a box object based on preferences and yield
        input yieldDict: Dictionary that tells the weekly yield
        """

        box = Box(self.id)
        
        for vegetable in vegetableList:
            amount = self.preferences[vegetable] *yieldDict[vegetable]/totalPreferences[vegetable]
            box.add(vegetable, amount)
            
        return box
        
    def weighted(self):
        """Returns a weighted dictionary of preferences"""
        weightedpref = {}
        total = 0
        for veg in vegetablePrices:
            total += self.preferences[veg]*vegetablePrices[veg]
        
        for veg in vegetablePrices:
            weightedpref[veg] = self.preferences[veg]/total * self.shares
        
        self.preferences = weightedpref

def get_distribution(userList, yieldDict):

    """returns a list of boxes
    yieldDict: weekly produce yield
    userList" list of users
    """
    totalPreference = {}
    for vegetable in vegetableList:
        totalPreference[vegetable] = 0
    
    boxList = []
    for user in userList:

        user.weighted() #this method weights the
        
        for vegetable in vegetableList:
            totalPreference[vegetable] += user.preferences[vegetable]
  
    
    
    for user in userList:
        boxList.append(user.get_box(yieldDict, totalPreference))
        
    return boxList
    
    
    
    