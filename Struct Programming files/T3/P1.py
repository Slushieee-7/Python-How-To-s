x = input("Enter a number: ")

while len(x) > 1:
    y = 0
    prevy = 0
    print("\n\n", "For loop starts here: ")
    for i in x:  
        print("Index now is " , i)
        prevy = y
        print("Previous y: ", prevy)
        y += int(i)
        print(prevy, " + ", i)
        print("The value of y is now: " , y, "\n")
    x = str(y)

print("The digital root is: " + x)
    
