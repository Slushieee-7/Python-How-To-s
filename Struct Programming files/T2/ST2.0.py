for i in range(5, 0, -1):
    a = ""
    b = ""
    for j in range(1, i + 1):
        a += str(j) + " "
        b += str(j * 2) + " "
    
    if i > 2:
        print(a)
        print(b)
    else:
        print(a)
print("\n\n End of number listing")