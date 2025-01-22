#Here is how booleans work in python

x = "hellow" 
y = bool(None) # This will return False because None is not True

print("The value of x is: " , bool(x) , " because it has a value in it")
print("The value of y is: " , y , " because it has no value in it")

#calling booleans in a function
def check(x):
    if x:
        return "The value is True"
    else:
        return "The value is False"

print(check("Hello")) 
print(check(None))


