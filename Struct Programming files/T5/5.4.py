print("Name: Rey Joshua Delos Reyes", "\n", "School: FEU Alabang", "\n", "Machine Problem - 4")

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

x = []
for i in arr:
    x.append(i * (arr.index(i) + 1))

print(x)