import os
import datetime

user = {
    'pin': 1653,
    'balance':2500
}

def widthdraw_cash():
    while True:
        amount = int(input("Enter Amount : "))
        if amount > user['balance']:
            print("Insufficient Amount : ")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Pesos successfully widthdrawn your remaining balance is {user['balance']} Pesos")
            print('')
            return False

def balance_enquiry():
    print(f"Amount Left is {user['balance']} Peso")
    print('')

is_running = True
is_quit = False

while is_running:  
    if os.path.exists ("pinchange.txt"):
        print('')
        print("Welcome to the Pythondex ATM")

        pin = int(input('Enter your PIN Number: '))

        if pin == user['pin']:
            while is_quit == False:
                print("what do you want to do")
                print(" Enter 1 to Widthdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to End Transaction \n Enter 4 to Change Pin")

                query = int(input("Select on the Menu list you want to do: "))

                if query == 1:
                    widthdraw_cash()
                elif query == 2:
                    balance_enquiry()
                elif query == 3:
                    print("Thank you for using the Pythondex ATM!")
                    is_quit = True
                    is_running = False
                elif query == 4:
                    admin = input("Enter admin username: ")
                    password = input("Enter admin password: ")
                    x = datetime.datetime.now()
                    status = "Pin Change"
                
                    with open ("pinchange.txt", "a") as q:
                        q.write(admin)
                        q.write("\t")
                        q.write(password)
                        q.write("\t")
                        q.write(str(x))
                        q.write("\t")
                        q.write(status)
                        q.write("\n")
                
                    print("Pin changed successfully!")
                    break
                else:
                    print("Please enter a correct value shown")
        else:
            print("Incorrect pin")
    else:
        open("pinchange.txt", "x")
        print("Pin change file created! Run the program again")