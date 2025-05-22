print("Name: Rey Joshua Delos Reyes", "\n", "School: FEU Alabang", "\n", "Machine Problem - 3")

arr = [30, 7, 30, 2, 88, 44, 60, 40, 1, 53, 100, 72, 86,
64, 40, 85, 3, 19, 63, 84, 17, 31, 95, 84, 99, 60,
85, 74, 65, 38, 43, 80, 39, 70, 8, 21, 32, 68, 64,
55, 88, 84, 49, 68, 70, 98, 21, 51, 3, 97]

x = 0
y = 0
for i in range(len(arr)):
    if arr[i] > 10:
        arr[i] = 666
        x += 1
    else:
        y += 1

print("Output is: ", arr)
print("Total equal values: ", x)
print("Total not equal values: ", y)
