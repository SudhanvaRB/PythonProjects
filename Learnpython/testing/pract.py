'''
Created on Feb 18, 2019

@author: subharad
'''
'''
memo ={}

def fact(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        x = fact(n-1) * n
        memo[n] = x
        return x
    
print(fact(20))
'''
'''

previous = {0: 0, 1: 1}


def fibonacci(n):
    if n in previous:
        return previous[n]
    else:
        val = fibonacci( n- 1) + fibonacci(n-2)
        previous[n] = val
        return val
print(fibonacci(20))



def fib(n):
    if n == 0:
        return 0
    elif n>=1 and n<=2:
        return 1
    else:
        return fib(n-1) + fib (n-2)    
    
print(fib(20))    

facto = {0:1 , 1:1 , 2:2 , 3:6}

def fac(n):
    if n in facto:
        return facto[n]
    else:
        val = n * fac(n-1)
        facto[n] = val
        return val

print(fac(19))
print(facto)
'''
'''
dict_str = {'stro':123}
print(dict_str['stro'])
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.keys())
print(inventory.values())
print(inventory.items())

alias_d = inventory
copy_alisa = inventory.copy()
alias_d['bananas'] = 400
print(inventory['bananas'])
'''

'''
str1 = 'Hello'
str2 ='World!'
li_en = list(enumerate(str1))
print(li_en)

from collections import defaultdict

text = 'Hello'
chars = defaultdict(int)

for char in text:
    chars[char] += 1
    
print(chars)

count = {}

example = "I like cake"

for i in example.split():
    count[i] = len(i)

print(count)

from collections import Counter
print(Counter('cats on wheels'))
    
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(sorted(inventory.values(), reverse= True))
inventory['melon'] = 100
print(inventory)

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
#dic1= dic2.copy()
dic4={}
for d in dic1,dic2,dic3:
    dic4.update(d)
print(dic4)

print(5 in dic4)
for key, value in inventory.items():
    print(key,value)
    
def dic_sqr(n):
    dic_comp = {i:i*i for i in range(1,n+1)}
    return dic_comp

print(dic_sqr(7))
mu = 1
for i in inventory.values():
    mu = mu * i
print(inventory)
inventory.popitem()
print(inventory)
'''
my_tuple = 3, 4.6, "dog"
a,b,c = my_tuple
print((my_tuple))
print(a)
print(("Repeat") * 3)

my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p'))
print(my_tuple.index('l'))
print('p' not in my_tuple)

print(list(enumerate(my_tuple)))

grocery = ['bread', 'milk', 'butter']
print((enumerate(grocery)))

for c,i in enumerate(grocery,10):
    print(c,i)
    
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory.popitem()
print(inventory)
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
dict1 = {}
for i in keys:
    for j in values:
        dict1[i] = j
print(dict1)
 
for i in len(keys+1):
    for j in len(values+1):
        dict1 = keys[i] : values[j]
        print(dict1)

     
    
    

    





