'''
Created on Feb 15, 2019

@author: subharad
'''
from math import sqrt
class Person:
    def __init__(self,name):
        self.name = name
        
    def say_hi(self):
        print("Hi" , self.name)
    pass  # An empty block

p = Person("Sudhanva")
#p.say_hi()

class Robot:
    population = 0
    
    def __init__(self,name):
        self.name = name
        print("initializing {}".format(self.name))
        Robot.population += 1
        
    def die(self):
        print("{} is being destroyed".format(self.name))
        Robot.population -=1
        
        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("there are still {:d} working ".format(Robot.population))
            
    def say_hi(self):
        print("{} is saying Hi".format(self.name))
            
    @classmethod
    def how_many(cls):
        print("we have {:d} robots".format(Robot.population))
        
robo1 = Robot("Droid")
robo1.say_hi()
Robot.how_many()

robo2 = Robot("apple")
robo2.say_hi()
Robot.how_many()
robo1.die()
robo2.die()
Robot.how_many()

l=[]
for i in range(2000,3201):
    if (i % 7 == 0) and (i % 5 !=0):
        l.append(str(i))
        
print(','.join(l))

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(7))

def dict_create(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    print(d)
        
dict_create(7)

'''
nos = input('enter nos:')
l = nos.split(',')
t = tuple(l)


print(l)
print(t)
'''

C = 50
H = 30
D = 100
print(round(sqrt((2 * C * D)/H)))



        
        

