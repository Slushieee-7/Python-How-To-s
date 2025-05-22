import numpy as np

print("Name: Rey Joshua Delos Reyes", "\n", "School: FEU Alabang", "\n", "Machine Problem - 2")
arr = [18, 19, 20]
print("Original list: ", arr)

arr[1] = 17
print("A. ", arr)

arr.append(4)
arr.append(5)
arr.append(6)
print("B. ", arr)

arr.pop(0)
print("C. ", arr)

arr.sort()
print("D. ", arr)

x = arr.copy()
print("E. ", x)

arr[3] = 25
print("F. ", arr)