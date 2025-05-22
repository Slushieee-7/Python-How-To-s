import numpy as np

arr = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39, 71, 55, 41,
95, 70, 48, 42, 32, 13, 35]
print("A. " , arr)

mean = np.mean(arr)
print("B. ", mean)

print("C. ", min(arr), max(arr))

s = set(arr)
print("D. ", sorted(s)[1], sorted(s)[-2])

x = 0
y = 0
for num in arr:
    if num % 2 == 0:
        x += 1
    else:
        y += 1
print("Even numbers in the array: ", x)
print("Odd numbers in the array: ", y)