x = input("Enter first string: ")
y = input("Enter second string: ")

def xyz_diff(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]:
            return i + 1
    if len(x) != len(y):
        return min(len(x), len(y))
    return -1 

print(xyz_diff(x, y))