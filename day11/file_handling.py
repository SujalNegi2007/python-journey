import os
import csv
from datetime import datetime
def database(user_activity):
    with open("database.txt","a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}], {user_activity}\n")
def window():
    print("\n+---------------------------------------+\n| To add data to the file   : Enter [1] |\n| To check data in the file : Enter [2] |\n| To Exit the program       : Enter [3] |\n| To Add to CSV File        : Enter [4] |\n| To Read CSV File          : Enter [5] |\n+---------------------------------------+")
def check():
    user_input = input("Enter your choice: ")
    database(f"User entered {user_input}.")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            database(f"User chose to add data to the file.")
            user_choice = input("Enter the file name in which you want to add the data: ")
            database(f"User entered [{user_choice}.txt] to check if it exists.")
            if os.path.exists(user_choice + ".txt"):
                database(f"{user_choice}.txt does exists.")
                user_data = input(f"Enter the data you want to the {user_choice}.txt: ")
                database(f"User entered [{user_data}] to add to [{user_choice}.txt] file.")
                with open(user_choice + ".txt", "a") as f:
                    f.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M')}], {user_data}\n")
            else:
                print(f"{user_choice}.txt doesn't exists!")
                database(f"[{user_choice}.txt] didn't exists.")
                user_option = input(f"Do You Want to create {user_choice}.txt? Only answer in (yes/no): ").capitalize().strip()
                yes_no(user_option,user_choice)
        elif user_input == 2:
            user_choice = input("Enter the name of file of which you want to check data of: ")
            database(f"User chose to check data in the file.")
            if os.path.exists(user_choice + ".txt"):
                if os.path.getsize(user_choice + ".txt") != 0:
                    with open(user_choice + ".txt", "r") as f:
                        content = f.read()
                        print(content)
                    database(f"user read the data from [{user_choice}.txt] successfully.")
                else:
                    database(f"The file User chose was found to be empty.")
                    print("File is empty so we can't read anything!")
            else:
                database(f"The file user chose didn't exists.")
                print(f"{user_choice} doesn't exists!")
        elif user_input == 3:
            database(f"User chose to exit.")
            print("Exiting...\nClosing Files...\nSaving data...")
            return False
        elif user_input == 4:
            csv_input = input("Enter the file name: ")
            header = ["name", "city", "age"]
            name = input("Enter Your Name: ").strip()
            city = input("Enter the Name of City in which You Live: ").strip()
            age = input("Enter Your Age: ").strip()
            data = {"name" : name, "city" : city, "age" : age}
            database(f"User entered the following details => {data}.")
            if os.path.exists(csv_input + ".csv"):
                if os.path.getsize(csv_input+".csv") == 0:
                    database(f"User chose to enter the data in [{csv_input}.csv] file which exists but the file is empty.")
                    m = True
                else:
                    m = False
                    database(f"User chose to enter the data in [{csv_input}.csv] file which exists.")
            else:
                m = True
                database(f"User chose to enter the data in [{csv_input}.csv] file by creating the file.")
            with open(csv_input + ".csv", "a", newline = "") as f:
                obj = csv.DictWriter(f, fieldnames = header)

                if m:
                    obj.writeheader()
                obj.writerow(data)
        elif user_input == 5:
            csv_view = input("Enter the name of file you want to check: ")
            if os.path.exists(csv_view+".csv"):
                if os.path.getsize(csv_view+".csv") != 0:
                    database(f"User read {csv_view}.csv")
                    with open(csv_view+".csv", "r", newline = "") as f:
                        reader = csv.DictReader(f)
                        for i, r in enumerate(reader,1):
                            print(f"row {i}=> Name : {r['name']} | City : {r['city']} | Age : {r['age']} ")
                else:
                    print("File is empty!")
                    database(f"User tried to read {csv_view}.csv but it was found to be empty.")
            else:
                print(f"There is no file avaliable with the name of [{csv_view}.csv]")
                database(f"User tried to read {csv_view}.csv but it was found that it doesn't exists.")
                
            
    else:
        print(f"{user_input} is not a number")
        database(f"{user_input} was not in options.")

def yes_no(user_option,user_choice):
    while True:
        if user_option == "Yes":
            database(f"User created {user_choice}.")
            print("File Has Been Successfully Created!")
            with open(user_choice + ".txt", "a") as g:
                pass
            user_input = input(f"What Do You Want to add to the {user_choice}.txt: ").strip()
            database(f"User Entered {user_input} to enter in {user_choice}.txt")
            with open(user_choice + ".txt", "a") as g:
                g.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}], [{user_input}] has been added.\n")
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
        break
