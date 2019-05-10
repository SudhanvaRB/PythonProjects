'''
Created on Feb 11, 2019

@author: subharad
'''
list_my = list([1,2,[1.1,2.2]])
print(list_my[2][1])

list_comp = [i for i in range(1,6)]
print(list_comp)
############################################################################
listofCountries = ["India","America","England","Germany","Brazil","Vietnam"]
first_letters = [i[0] for i in listofCountries]
print(first_letters)

new_lis=[]
for i in listofCountries:
    new_lis.append(i[0])
print(new_lis)

##########################################################################
cond = [x+y for x in 'get' for y in 'set' if x!='t' and y!='e']
print(cond)

lt=[]
for i in 'get':
    for j in 'set':
        if i!='t' and j!='e':
            lt.append(i + j)
print(lt)

#############################################################################

init_list = [0]*3
print(init_list)

two_d = [[0]*3]*3
print(two_d)

lit =[[0]*3 for i in range(3)]
print(lit)

L1 = [2,3]
L2 = [1,2]

L1.extend(L2)
print(L1)
theList = [1, 2, 3, 4, 5, 6, 7, 8]
print(theList[::-1])

#################################################
theList = [1, 2, 3, 4, 5, 6, 7, 8]
for index, element in enumerate(theList):
    print(index, element)
    
for index in range(len(theList)):
    print(index)
    
it = iter(theList)
print(iter(it))

###############################
theList = ['a','e','i','o','u']
theList.sort(reverse=True)
theList.count

######################

a = ['a', 'b']
#a[0:2] = 'cat'
a.insert(0 ,'cat')
print(a)

person = {}
type(person)

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

print(person['children'][-1])
  
dic_ex = {'abc':'z',2:1,2:3}
print(dic_ex)
dit = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print(dit[(1,2)])

#####################################################################

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3,7] 
marks = [ 40, 50, 60, 70 ] 

for n,r,m in zip(name,roll_no,marks):
    print("Name:%s         Rollno:%d         Marks:%d" %(n,r,m))

'''
mapped = zip(name,roll_no,marks)
mapped = list(mapped)
print(mapped)

nam,rol,marl=zip(*mapped)
print(list(nam))
print(rol)
print(marl)
'''
    
key_value ={}     
   
# Initializing the value  
key_value[2] = 56       
key_value[1] = 2 
key_value[5] = 12 
key_value[4] = 24
key_value[6] = 18      
key_value[3] = 323 
print(sorted(key_value.items()))


dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 

print(dict1.update(dict2))
print(dict1)
print({**dict1,**dict2})


def myfunc(*some_arg):
    print(some_arg)
    
myfunc('Hello','xy',123)

# Python program to illustrate 
# *kargs for variable number of keyword arguments 

def myFun(**kwargs): 
    for key, value in kwargs.items(): 
        print ("{} is {}".format(key,value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')     



def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point      
  
# Driver code to test above generator  
# function 
for num in nextSquare(): 
    if num > 200: 
        break    
    print(num) 


def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
x = fib(6) 
print(x)
  
# Iterating over the generator object using next 
print(x.__next__()) # In Python 3, __next__() 
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

squared_list = (x**2 for x in range(5))
for i in squared_list:
    print(i)



# Check the type
print(type(squared_list))
#print(len(squared_list))


def cube_number(val):
    for i in val:
        yield(i**3)

cubes = cube_number([1,2,3,4])


for i in cubes:
    print(i) 
    
print(type(cubes))

def addi(x,y,z=0):
    return x+y+z

#print(addi(1))


class Country():
    def __init__(self,capital,language):
        self.capital = capital
        self.language = language
    
    def printcapital(self):
        print("Capital is {}".format(self.capital))
        
    def printlanguage(self):
        print("National Language is {}".format(self.language))
        
class CountryName(Country):
    def __init__(self,country,capital,language):
        self.country = country
        self.capital = capital
        self.language = language
    
    def printcapital(self):
        print("Capital is {}".format(self.capital))

obj_co = Country('NewDelhi', 'hindi')
ob_2 = CountryName('India','NewDelhi', 'hindi')
print(ob_2.capital)
print(ob_2.country)
print(ob_2.language)
ob_2.printcapital()
print(obj_co.capital)


class India():
    def capital(self):
        print("New Delhi")
    
    def language(self):
        print("Hindi")
        
class USA():
    def capital(self):
        print("New York")
    
    def language(self):
        print("English")
        
def func(obj):
    obj.capital()
    obj.language()

    
obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
'''

for i in (obj_ind,obj_usa):
    i.capital()
    i.language()

class Birds():
    def intro(self):
        print("there are many type of birds")
    
    def flight(self):
        print("almost all birds can fly")
        
class Sparrow(Birds):
    def flight(self):
        print("sparrow can fly")
        
class Ostrich(Birds):
    def flight(self):
        print("ostrich cannot fly")
        
obj_bird = Birds()
obj_spro = Sparrow()
obj_ost = Ostrich()
obj_spro.flight()

'''

dictionary = {} 
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1

print(dictionary)

sum = 0
for k in dictionary:
    sum = sum + dictionary[k]
    
print(sum)

check1 = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
check2 = check1 
check3 = check1[:]

check2[0] = 'code'
check3[3] ='prent'

print(check1)
print(check2)
print(check3)


def gfg(x,l=[]): 
    for i in range(x): 
        print(i)
        l.append(i*i) 
    print(l) 

#gfg(2) 
gfg(3,[3,2,1]) 
gfg(3) 

    