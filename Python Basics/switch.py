#switch cases in python
#there are no switch cases in python, but here are some alternatives

#using the elif statements 
def switch(value):
    if value == 1:
        return 'one'
    elif value == 2:
        return 'two'
    elif value == 3:
        return 'three'
    else:
        return 'unknown value'
    
ans = input("Enter a value: ")
print("The value entered is", switch(int(ans)))

#using dictionary mapping (which are defining each cases possible)
def letter_a():
    return "A"
def letter_b():
    return "B"
def letter_c():
    return "C"
def letter_d():
    return "D"
def default():
    return "Unknown letter"

def dict(value):
    switcher = {
        1: letter_a,
        2: letter_b,
        3: letter_c,
    }
    # Get the function from switcher dictionary
    return switcher.get(value, default)()
    # Execute the function

print("The letter in that number is:", dict(2)) #outputs the function of letter_b which is "B"

#lastly, if ur python's version is 3.10+, u can freely use a switch case statement
def switch(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Unknown value"
        

result = switch(3) #which would output "Three"
print(result)