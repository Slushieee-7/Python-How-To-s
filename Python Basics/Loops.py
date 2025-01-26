#loops in python
#indentation is important when handling loops in python

x = 100
y = 200
z = 250
if x > y: #if loop
    print("x is greater than y")
elif x < y : #else if loop
    print("y is greater than x")
else: 
    print("x and y are equal")

#u can just write it in only one line (what psychopath does that)
if x == 100: print("x is equals to 100")

#short hand if loop (like translating a sentence to a code)
print("I am a 100") if x == 100 else print("I am not 100")

#we use "and" for another condition
if x < y and y < z:
    print("I am somewhere between 100 and 250")

#we use "or" for adding another condition (or just like how u use "or" in a sentence)
if x > y or y < z:
    print("I am somewhere between 100 and 250") #this would still be printed because, it may not pass the first condition, but it passed the second condition

#we use "not" just like how u use the word "not" in a sentence
if not x > y:
    print("x is not greater than y")

#nested if statement
if x == 100:
    print("I am a 100")
    if y == 200:
        print("Going to 200")
    else:
        print("I am not a 200")

#pass statement 
#this is used when u need a loop or if statement but u dont have any condition to check
for i in range(10):
    pass #this would just do nothing and just pass the loop

#while loops
a = 1
while a < 5:
    print(a)
    a += 1
    
#break statements
b = 2
while b < 10:
    print(b)
    b += 1
    if b == 5: #if b is 5, it would stop the loop
        break

#continue statements (or when u want to skip a value)
c = 0
while c < 10:
    c += 1
    if c % 2:
        continue #this would skip the value of c if it is odd
    print(c) #this would only print the even values of c
