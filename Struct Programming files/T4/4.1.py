print("Name: Rey Joshua M. Delos Reyes")
print("School: FEU Alabang")
print("Machine Problem - 1")

while True:
    try:
        x = int(input("Enter the length: "))
        y = int(input("Enter the width: "))

        if x < 0 or y < 0:
            print("The number is not a positive integer")
        else:
            area = x * y
            print("The area of the Rectangle is:", area)

    except ValueError:
        print("Input the correct data format")
