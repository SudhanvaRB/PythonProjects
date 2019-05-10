'''
Created on Mar 22, 2019

@author: subharad
'''
import re
from re import split


str1 = 'tiiii  piiig'
match = re.search(r'ii+\s*pi+', str1)

if match:
    print('found',match.group())
else:
    print("no match")
    

class Dog:
    
    species = 'mammal'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
    def desc(self):
        return "{} is {} years old".format(self.name,self.age)
    
    def dog_sound(self,sound):
        return "{} makes {} sound".format(self.name,sound)
    

class Bulldog(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)
    

        
print(Dog.species)
a = Dog("juli",4)
b = Dog("etc",6)
c = Dog("piio",9)
print("{} is of age {}".format(a.name,a.age))

print(a.dog_sound("bow bow"))
print(b.desc())

def max_age(*args):
    return max(args)
print(max_age(a.age,b.age,c.age))
if a.species == 'mammal':
    print("yes")

jim = Bulldog("julia",12)

print(jim.run("very fast"))
print(jim.dog_sound("bowwwwwwwwww"))
print(jim.desc())
print(isinstance(jim,Dog))

pattern = r"Cookie"
sequence = "Cookie"
print(re.search(r'<.*?>', '<h1>TITLE</h1>').group())

email_address = "Please contact us at: xyz@datacamp.com"
address = re.sub(r'\w+@\w+.\w+','sud@test.com',email_address)

print(address)

p = re.compile('[a-zA-Z]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

P = re.compile('\d+')
print(P.findall('I went to him at 11 A.M. on 4th July 1886'))

z = re.compile('\w+')
print(z.findall('I went to him at 11 A.M., he said *** in some_language.'))

pt = re.findall(r'\W','A.M.,***_\.')
print(pt)
    
A = re.compile('ab?')
print(A.findall('ababbaabbb'))

print(re.split('\W+', 'Words, words , Words')) 
print(re.split('\W+', "Word's words,t Words")) 
print(re.split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE)) 
print(re.split('[a-z]+', 'Aey, Boy oh boy, come here')) 

print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 

print(re.subn('ub', '~*' , 'Subject has Uber booked already')) 
t = re.subn('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE) 
print(t) 
print(len(t))

print(re.escape("This is Awseome even 1 AM")) 

print(re.escape("I Asked what is this [a-9], he said \t ^WoW")) 

regex = r"([a-zA-Z]+) (\d+)"
  
match = re.search(regex, "I was born on June 24").group() 

print(match)

'''
file = open("C:/Users/subharad/Desktop/sample.txt",'a')
file.write("he is good")
file.write("he is tall")
file.close()
'''
'''
file = open("C:/Users/subharad/Desktop/sample.txt",'w',encoding="utf-8")
file.write("writing to file\n")
file.close()
#file.read()
file = open("C:/Users/subharad/Desktop/sample.txt",'r')
print(file.read())

'''

'''
with open("C:/Users/subharad/Desktop/sample.txt",'r') as f:
    print(f.read())
'''

fruits=["Orange\n","Banana\n","Apple\n"]
file = open("C:/Users/subharad/Desktop/sample.txt",'a+',encoding='utf-8')
file.writelines(fruits)
print("Tell the byte at which the file cursor is:",file.tell())
file.seek(4,0)
for i in file:
    print(i)

file.close() 

'''
file = open("C:/Users/subharad/Desktop/sample.txt",'r')
print(file.read())
'''


import json
my_data=["Hafsa Jabeen","Reading and writing files in python",78546]
json.dumps(my_data)

with open("C:/Users/subharad/Desktop/sample.json","w") as f:
    json.dump(my_data,f)
f.close()

with open("C:/Users/subharad/Desktop/sample.json",'r') as f:
    print(json.load(f))
f.close()


arr = {1, 2, 3}

sum = 0
for i in arr:
    sum+=i
print(sum)

def add(inp):
    sum = 0
    for i in inp:
        sum+=i 
    print(sum)

add([7,8,10,10])

def largest(val,n):
    max_val = val[0]
    for i in range(1,n):
        if val[i] > max_val:
            max_val = val[i]
    return max_val

inp = [10,700,80,900,11]
n = len(inp)
print(largest(inp,n))
    
li = [9,8,7,6,5,4,3,2,1]
li2=[]
for i in range(2,len(li)):
    li2.append(li[i])
    #print(li[i])

for i in range(0,2):
    li2.append(li[i])
    print(li[i])

print(li2)

def rot(som,x):
    li2=[]
    for i in range(x,len(som)):
        li2.append(som[i])
    for i in range(0,x):
        li2.append(som[i])
    print(li2)

v = [9,8,7,6,5,4,3,2,1]
print(v.pop(3))
print(v)
n = 3
'''
rot(v,n)

print(v[len(v)-1])

temp = v[0]
v[0] = v[len(v)-1]
v[len(v)-1] = temp 
print(v[len(v)-1])
print(v)
'''    

list1= [10, 11, 12, 13, 14, 15] 
print(list1.reverse())
list2=[]
for i in range(1,len(list1)+1):
    list2.append(list1[-i])
print(list2)

lst = [20, 6, 7, 10, 12, 20, 10, 28, 20]
lst2=[]
c
items = [1,1,1,4,4]

stats = {}
for i in items:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

print(stats)
    

    

    
