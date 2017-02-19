import algorithm
from vegetables import *

user1 = algorithm.User(1, {'onions':3, 'potatoes':2, 'celery':5, 'carrots':4, 'squash': 3}, 1)
user2 = algorithm.User(2, {'onions':3, 'potatoes':5, 'celery':2, 'carrots':5, 'squash': 2}, 1)
user3 = algorithm.User(3, {'onions':6, 'potatoes':4, 'celery':0, 'carrots':7, 'squash': 1}, 1)

userList = [user1, user2, user3]

yielddict = {'onions': 20, 'potatoes':50, 'celery': 10, 'carrots':30, 'squash': 10}

boxlist = algorithm.get_distribution(userList, yielddict)

for box in boxlist:
    print box.userid, box.items
    total = 0
    for item in box.items:
        total += box.items[item] * vegetablePrices[item]
    print total
