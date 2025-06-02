class project_details:
    def __init__(self, id, title, size, priority):
        self.id = id
        self.title = title
        self.size = size
        self.priority = priority



print("\t\t Menu \n")
print(" 1. Input Project Details \n", "2. View Projects \n", "3. Scheduled Projects \n", "4. Get a Project \n", "5. Exit \n")

n = int(input("Enter your choice: "))
match(n):
    case 1:
        print ("Welcome to Input project details")
        exit
    case 2:
        print(" 1. One Project \n", "2. Completed Projects \n", "3. All Projects \n")
        y = input("Enter your choice: ")
        
        if (y == "1"):
            x = input("Enter an ID: ")
              
    case 3: 
        print(" 1. Create Schedule \n", "2. View Schedule \n")
        x = input("Enter your choice: ")
    case 4:
        print("Get a Project")
    case 5:
        exit
        
