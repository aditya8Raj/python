import random

# This is a comment
"""
This is
multi line
comment
"""

# print function 
print("Hello World")  #outputs: Hello World

# 🔴 Variables
x = 5
y = 2
print(x)  # outputs: 5
print(y)  # outputs: 2

# Assign multiple values to multiple variables:
a, b, c = "Apple", "Mango", "Banana"
print(a)  # Outputs: Apple
print(b)  # Outputs: Manga
print(c)  # Outputs: Banana

# You can assign One Value to Multiple  Variables
x = y = z = "Saturn"
print(x)  # outputs: Saturn
print(y)  # outputs: Saturn
print(z)  # outputs: Saturn

# Unpacking
fruits = ["Orange", "Kiwi", "Watermellon"]
x, y, z = fruits
print(x)  # outputs: Orange
print(y)  # outputs: Kiwi
print(z)  # outputs: Watermellon

# 🔴 Concatanation
name = "Aditya"
print("My name is " + name )

# 🔴 Data Types
x = 8
print(type(x))

# 🔴 Random module
print(random.randrange(1, 10))  #prints random number between 1-10

# 🔴 Python Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)  # ouputs: 1
print(y)  # ouputs: 2
print(z)  # ouputs: 3

x = float(1)   # x will be 1.0
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
print(x)  # outputs: 1.0
print(y)  # outputs: 2.8
print(z)  # outputs: 3.0

x = str("s1")  # x will be 's1'
y = str(2)     # y will be '2'
z = str(3.0)   # z will be '3.0'
print(x)  # outputs: s1
print(y)  # outputs: 2
print(z)  # outputs: 3.0

# 🔴 Strings
a = "Hello"
print(a)  # outputs: Hello
# Multiline Strings
a = """This is a multiline string,
come back, I still miss you,
but whocares,
hahaha"""
print(a)
# Strings are Arrays
name = "Aditya"
print(name[1])  # outputs: d
# String length with len() function
favFruit = "Watermellon"
print(len(favFruit))   # outputs: 11
#check if a certain phrase or character is present in a string
txt = "God is watching."
print("NOT" in txt)  # outputs: False
#check if a certain phrase or character is NOT present in a string
newTxt = "Saturn is my favourite planet."
print("Earth" not in newTxt)  # outputs: True
# Slicing
b = "Hello World!"
print(b[2:5])  # outputs: llo
#slice from the start
print(b[:5])  # outputs: Hello
#slice to the end
print(b[2:])  # outputs: llo World!
#Negative Indexing
print(b[-5:-2])  # outputs: orl

a = "Hello World"
#upper case
print(a.upper())  # outputs: HELLO WORLD
#lower case
print(a.lower())  # outputs: hello world
#remove whitespace
print(a.strip())  #outputs: Hello World
#replace string
print(a.replace("H", "M"))  # outputs: Mello World
#split string
print(a.split(","))  # outputs: ['Hello World']

# 🔴 String format
age = 19
txt = "My name is Aditya, I am {} years old."
print(txt.format(age))  # outputs: My name is Aditya, I am 19 years old.

# 🔴 Booleans
# true or false
print(10 > 9)   # Outputs: True
print(10 == 9)  # Outputs: False
print(10 < 9)   # Outputs: False

print(bool("Hello"))  # Outputs: True
print(bool(17))       # Outputs: True

# 🔴 Lists
fruits = ["apple", "mango", "banana"]
print(fruits)  # outputs: ["apple", "mango", "banana"]

print(fruits[2])   # outputs: banana
print(len(fruits)) # outputs: 3
fruits[0] = "grapes"  # first element is "grapes" now
print(fruits)    # outputs: ["grapes", "mango", "banana"]

print(type(fruits))  # outputs: <class 'list'>
# sort list  -- this sorts the list alphanumerically
fruits.sort()
print(fruits)   # outputs: ['banana', 'grapes', 'mango']

mynumbers = [190, 220, 87, 54, 97]
mynumbers.sort()
print(mynumbers)   # outputs: [54, 87, 97, 190, 220]

# sort list in decending order
mynumbers.sort(reverse = True)
print(mynumbers)   # outputs:  [220, 190, 97, 87, 54]

#join two lists
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)  # outputs:  ['a', 'b', 'c', 'd', 1, 2, 3]

# 🔴 Tuples
myTuple = ("apple", "mango", "grapes")
print(myTuple)  # outputs: ('apple', 'mango', 'grapes')

print(type(myTuple))  # outputs: <class 'tuple'>

print(myTuple[1])  # outputs: mango

#most of the things are same in tuples and lists

# 🔴 Set
mySet = {"apple", "mango", "banana"}
print(mySet)  # outputs: {'apple', 'mango', 'banana'}

print(type(mySet))  # outputs: <class 'set'>

# 🔴 Dictionaries
myDict = {
    "name": "Aditya",
    "age": 19,
    "city": "Mumbai"
}
print(myDict)  # outputs: {'name': 'Aditya', 'age': 19, 'city': 'Mumbai'}

print(myDict["name"])  # outputs: Aditya

print(len(myDict))  # outputs: 3

# nested dictionary
myFamily = {
    "child1": {
        "name": "Aditya",
        "age": 19
    },
    "child2": {
        "name": "Rohan",
        "age": 23
    }
}

# 🔴 If Else

a = 33
b = 200
if a > b:
  print("a is greater than b")
else:
    print("b is greater than a")  # outputs: b is greater than a

# elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
    print("a and b are equal")  # outputs: a and b are equal

# Short Hand If
if a > b: print("a is greater than b")  # outputs: b is greater than a

# Short Hand If Else
print("A") if a > b else print("B")  # outputs: B

# And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")  # outputs: Both conditions are True

# Or
if a > b or a > c:
  print("At least one of the conditions is True")  # outputs: At least one of the conditions is True

# Not
if not a > b:
  print("b is greater than a")  # outputs: b is greater than a

# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")  # outputs: and also above 20!
  else:
    print("but not above 20.")  # outputs: but not above 20.

# Pass
a = 33
b = 200

if b > a:
    pass

# 🔴 While Loop

i = 1
while i < 6:
  print(i)
  i += 1

# break
i = 1
while i < 6:
   print(i)
   if i == 3:
      break
   i += 1

# continue
i = 0
while i < 6:
   i += 1
   if i == 3:
      continue
   print(i)

# else
i = 1
while i < 6:
   print(i)
   i += 1
else:
   print("i is no longer less than 6")

# 🔴 For Loop

fruits = ["apple", "mango", "grapes"]
for item in fruits:
 print(item)

#looping through a string
for x in "banana":
   print(x)

# break statement in for loop
fruits = ["apple", "mango", "grapes", "banana"]
for x in fruits:
   print(x)
   if x == "grapes":
      break          #only apple mango grapes will be printed
   

fruits = ["apple", "mango", "grapes", "banana"]
for x in fruits:
   if x == "grapes":
      break
   print(x)

# continue statement
cars = ["Porsche", "Mustang", "GTR"]
for x in cars:
   if x == "Mustang":
      continue
   print(x)

# range() function
for x in range(9):
   print(x)

print("---------")

for x in range(4, 9):
   print(x)

print("---------")

for x in range(4, 30, 9):
   print(x)

# nested for loop:
foods = ["Poha", "Panner", "Kheer"]
taste = ["carbs", "protein", "sugarryy"]

for x in foods:
   for y in taste:
      print(x, y)

# pass statement
for x in [0, 1, 2]:
   pass

# 🔴 Functions

# creating a function
def my_func():
 print("This is a function")

#calling a function
my_func()  # outputs: This is a function
my_func()  # outputs: This is a function

#arguments in functions
def sum_fun(x, y):
   print(x + y)

sum_fun(2, 6)  #outputs: 8
sum_fun(5, 9)  #outputs: 14

# arbitrary arguments, *args
def my_function(*kids):
   print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")

#combine positional-only and keyword-only
def my_function(a, b, /, *, c, d):
   print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)  #outputs: 26

# 🔴 Lambda

x = lambda a : a + 10
print(x(5))     # outputs: 15

y = lambda j, k : j * k
print(y(4, 9))   # outputs: 39

# 🔴 Arrays

cars = ["Ford", "Volvo", "BMW"]
print(cars)
x = len(cars)
print(x)

for x in cars:
   print(x)

cars.append("Honda")
print(cars)

cars.pop(1)
print(cars)

# 🔴 Classes/Objects

#creating a class
class myClass:
   x = 5

#use class to create objects
p1 = myClass()
print(p1.x)

# __init__() Function
class Person:
   def __init__(self, name, age):
      self.name  = name
      self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# 🔴 User Input

username = input("Enter username: ")
print("Username is: " + username)
