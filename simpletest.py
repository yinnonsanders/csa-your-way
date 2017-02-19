import algorithm
from vegetables import *
import random
import math

user1 = algorithm.User(1, {'onions':1, 'potatoes':1, 'celery':1, 'carrots':1, 'squash': 1}, 1)
user2 = algorithm.User(2, {'onions':1, 'potatoes':1, 'celery':1, 'carrots':1, 'squash': 1}, 1)
user3 = algorithm.User(3, {'onions':1, 'potatoes':1, 'celery':1, 'carrots':2, 'squash': 1}, 1)


userList = []

for user in range(25):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)
    d = random.randint(0, 10)
    e = random.randint(0, 10)
    userList.append(algorithm.User(user, {'onions':a, 'potatoes':b, 'celery':c, 'carrots':d, 'squash':e}, 1))

yielddict = {'onions': 50, 'potatoes':50, 'celery': 50, 'carrots':50, 'squash': 50}

boxlist = algorithm.get_distribution(userList, yielddict)

totallist =[]
for box in boxlist:
    #print box.userid, box.items
    total = 0
    for item in box.items:
        total += box.items[item] * vegetablePrices[item]
    totallist.append(total)
    print total
    
#print sum(totallist)/len(totallist)

# totalprice = 0
# for items in yielddict:
#     totalprice += yielddict[items] * vegetablePrices[items]
# print totalprice