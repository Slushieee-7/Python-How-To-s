# f = open("testfile.txt", "x") #creates a file named "testfile.txt"

name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")
school = input("Enter your school: ")
course = input("Enter your course: ")
    
with open("testfile.txt", "w") as q: #writes on the file
    q.write("Name \t")
    q.write("Age \t")
    q.write("City \t")
    q.write("School \t")
    q.write("Course \t\n")  
    q.write(name)
    q.write(" \t")
    q.write(str(age))
    q.write(" \t\t")
    q.write(address)
    q.write(" \t")
    q.write(school)
    q.write(" \t")
    q.write(course) 

choi = input("Enter another record? Y/N ")

while (choi == "Y" or choi == "y"):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    address = input("Enter address: ")
    school = input("Enter your school: ")
    course = input("Enter your course: ")
    
    with open("testfile.txt", "a") as q: #writes on the file
        q.write("\n")
        q.write(name)
        q.write(" \t")
        q.write(str(age))
        q.write(" \t\t")
        q.write(address)
        q.write(" \t")
        q.write(school)
        q.write(" \t")
        q.write(course) 
    
    choi = input("Enter another record? Y/N ")

if (choi == "N" or choi == "n"):
    with open("testfile.txt") as w:
        print(w.read())
else:
    print("Invalid Choice")

# to remove the existing file    
# import os 
# os.remove("testfile.txt")
