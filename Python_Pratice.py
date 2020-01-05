'''
minus = lambda x,y : x-y
def min(a,b):
    return a-b
print(minus(9,5))

import datetime
time = datetime.datetime.now()
print(time)

'''
'''
import random
random_number = random.randint(1,10)
print(random_number)

random_num = random.random()*10
print(random_num)


lst = [15,68,52,98,78]
choice = random.choice(lst)
print(choice)
'''
'''
#Numpy
import numpy as np
a = 4
c = np.sqrt(a)
print(c)
d = np.convolve(a, c , mode='full')
print(d)


#platform
import platform as p
x = p.system()
print(x)

y = p.version()
print(y)


l = ["Hanad","kamil","Bilal","Shah","Aqib"]
d = {"Kamil":"Opner", "Aqib":"Opner", "Hanad":"One-Down","Noshu":"Two-Down","Asim":"Middle-Order"}
n = "This is the team"
def fun(n, *args, **team):
    print(n)

    for item in args:
        print(item)


    for key, value in team.items():
        print(f"{key} is a {value}")

fun(n, *l, **d)

'''

import time
initial = time.time()
a = 0
while a <= 10:
    print("I love pakistan")
    a += 1
print(f"While loop time is {time.time() - initial}")

initial2 = time.time()
for i in range(0,10):
    print("I love pakistan")
    
print(f"For loop time is {time.time() - initial2}")

time.sleep(2)



