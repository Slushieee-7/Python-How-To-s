# f = open("testfile.txt", "x") #creates a file named "testfile.txt"

name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")
school = input("Enter your school: ")
course = input("Enter your course: ")


with open("testfile.txt", "w") as q: #writes on the file
    q.write(name)
    q.write("\n")
    q.write(str(age))
    q.write("\n")
    q.write(address)
    q.write("\n")
    q.write(school)
    q.write("\n")
    q.write(course)

with open("testfile.txt") as w:
    print(w.read())

# to remove the existing file    
# import os 
# os.remove("testfile.txt")
