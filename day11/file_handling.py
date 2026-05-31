import os
from datetime import datetime
def database(user_activity):
    with open("database.txt","a") as f:
        f.write(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}], {user_activity}\n")
with open("database.txt","a") as f:
    pass
def window():
    print("\n+---------------------------------------+\n| To add data to the file   : Enter [1] |\n| To check data in the file : Enter [2] |\n| To Exit the program       : Enter [3] |\n+---------------------------------------+")
def check():
    user_input = input("Enter your choice: ")
    database(f"User entered {user_input}.")
    if user_input.isdigit():
        database(f"User input was found to be a integer.")
        user_input = int(user_input)
        if user_input == 1:
            database(f"User chose option 1 to add data to the file.")
            user_choice = input("Enter the file name in which you want to add the data: ")
            database(f"User entered {user_choice}.txt to check if it exists.")
            if os.path.exists(user_choice + ".txt"):
                database(f"{user_choice}.txt does exists.")
                user_data = input(f"Enter the data you want to the {user_choice}.txt: ")
                database(f"User entered {user_data} to add to {user_choice}.txt file.")
                with open(user_choice + ".txt", "a") as f:
                    f.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M')}], {user_data}\n")
            else:
                print(f"{user_choice}.txt doesn't exists!")
                database(f"{user_choice}.txt didn't exists.")
                user_option = input(f"Do You Want to create {user_choice}.txt? Only answer in (yes/no): ").capitalize().strip()
                yes_no(user_option,user_choice)
        elif user_input == 2:
            user_choice = input("Enter the name of file of which you want to check data of: ")
            if os.path.exists(user_choice + ".txt"):
                if os.path.getsize(user_choice + ".txt") != 0:
                    with open(user_choice + ".txt", "r") as f:
                        print(f.read())
                else:
                    print("File is empty so we can't read anything!")
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
            database(f"User created {user_choice}.")
            print("File Has Been Sucessfully Created!")
            with open(user_choice + ".txt", "x") as g:
                pass
            user_input = input(f"What Do You Want to add to the {user_choice}.txt: ").capitalize().strip()
            database(f"User Entered {user_input} to enter in {user_choice}.txt")
            with open(user_choice + ".txt", "w") as g:
                g.write(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}], {user_input} has been added.\n")
            break
        elif user_option == "No":
            database(f"User chose to go back by selecting no.")
            print("Going Back...")
            break
        else:
            database(f"User entered the wrong option.")
            print("Only Yes and No are avaliable options!")
            user_option = input(f"Do You Want to create {user_choice}.txt? Only answer in (yes/no): ").capitalize().strip()

while True:
    window()
    a = check()
    if a == False:
        print('Thank You For Visiting.')
        database("User exited the app.")
        break
