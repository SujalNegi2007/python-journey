import os
from datetime import datetime
def window():
    print("+---------------------------------------+\n| To add data to the file   : Enter [1] |\n| To check data in the file : Enter [2] |\n| To Exit the program       : Enter [3] |\n+---------------------------------------+")
def check():
    user_input = input("Enter your choice: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            user_choice = input("Enter the file name in which you want to add the data: ")
            if os.path.exists(user_choice):
                user_data = input(f"Enter the data you want to the {user_choice}: ")
                with open(user_choice, "a") as f:
                    f.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M')}] => {user_data}\n")
            else:
                print(f"{user_choice} doesn't exists!")
                user_option = input(f"Do You Want to create {user_choice}? Only answer in (yes/no): ").capitalize().strip()
                yes_no(user_option,user_choice)
        elif user_input == 2:
            user_choice = input("Enter the name of file of which you want to check data of: ")
            if os.path.exists(user_choice):
                with open(user_choice, "r") as f:
                    print(f.read())
            else:
                print(f"{user_choice} doesn't exists!")
        elif user_input == 3:
            print("Exiting...\nClosing Files...\nSaving data...")
            return False
            
    else:
        print(f"{user_input} is not a number")
def yes_no(user_option,user_choice):
    while True:
        if user_option == "Yes":
            g = open(user_choice, "x")
            g.close()
            break
        elif user_option == "No":
            break
        else:
            print("Only Yes and No are avaliable options!")
            user_option = input(f"Do You Want to create {user_choice}? Only answer in (yes/no): ").capitalize().strip()

while True:
    window()
    a = check()
    if a == False:
        print('Thank You For Visiting.')
        break
