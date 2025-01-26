#continue statements (or when u want to skip a value)
c = 0
while c < 10:
    c += 1
    if c % 2:
        continue #this would skip the value of c if it is even
    print(c) #this would only print the even values of c