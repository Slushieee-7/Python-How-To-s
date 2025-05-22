import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


def main():
    print("Name: Rey Joshua M. Delos Reyes")
    print("School: FEU Alabang")
    print("Machine Problem - 2")
    
    while True:
        try:
            radius = float(input("Enter the radius of the circle (positive number only): "))
            
            if radius < 0:
                print("The number is not a positive integer")
            else:
                circle = Circle(radius)
                area = circle.area()
                perimeter = circle.perimeter()
                
                print(f"The area of the circle is: {area:.2f}")
                print(f"The perimeter (circumference) of the circle is: {perimeter:.2f}")
                break  

        except ValueError:
            print("Input the correct data format")

if __name__ == '__main__':
    main()
