#this is how u can comment in python

#this is how to print in python
print("Part 1: Hello, World!")

#indentation is important in python
#indentation is used to define a block of code
if 5 > 3:
    print("Part 2: 5 is greater than 3")  #this would be an error if there is no indention

#variables in python
x = 4
y = 5
print ("Part 3:", x + y)  #this would print 9
                             #to concatenate strings or numbers together, instead of using +, in python, we use the comma (,)

#u can also use data types to specify the data types of the variable
x = int(5) 
y = float(2.5)
z = str(20)
print ("Part 4:", "int:", x, "float:", y, "string:", z)

#assigning mulitple values to multiple variables
x, y, z = 1, 2, 3
print ("Part 5:", x, y, z)

#unpacking a collection
fruits = ["watermelon", "apple", "banana", "grapes", "mango"]
x, y, z, *other = fruits #we use *other to include other values in the collection
basket = x, y, z, *other
print ("Part 6A:", *other) #prints out grapes and mango 
print ("Part 6B:", basket) 

#Three numeric data types in python
x = 9 #int
y = 3.14 #float
z = 3.14j #complex number

#to check what data type the each variable is, use type(variable name):
print ("Part 7A:", x, " is a ", type(x))
print ("Part 7B:", y, " is a ", type(y))
print ("Part 7C:", z, " is a ", type(z)) 

#to convert these data types use:
a = float(x) #converts int to float
b = int(y) #converts float to int
c = complex(x, y) #converts the int and float to complex
print ("Part 8A:", a, " is a ", type(a))
print ("Part 8B:", b, " is a ", type(b))
print ("Part 8C:", c, " is a ", type(c)) #puts the two numbers, 9 and 3.14, into one parentheses then adds a "j" at the end of the last nnumber

#to generate random numbers
import random #import the library
print("Part 9 (Random Numbers):",random.randrange(1, 20)) #prints a random number from 1-20







