import os
import csv
from datetime import datetime
import logging

logging.basicConfig(
    filename = 'app.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def window():
    print("\n" + "+" + "-"*138 + "+" + "\n" + 
          "| " + "To add data to the file   : Enter [1]".center(136) + " |" + "\n" + 
          "| " + "To check data in the file : Enter [2]".center(136) + " |" + "\n" + 
          "| " + "To Exit the program       : Enter [3]".center(136) + " |" + "\n" + 
          "| " + "To Add to CSV File        : Enter [4]".center(136) + " |" + "\n" + 
          "| " + "To Read CSV File          : Enter [5]".center(136) + " |" + "\n" + 
          "+" + "-"*138 + "+" + "\n")
def check():
    user_input = input("Your Reply: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            logging.info(f"User chose to add data to the file.")
            user_choice = input("Enter the file name in which you want to add the data: ")
            if os.path.exists(user_choice + ".txt"):
                logging.info(f"User entered [{user_choice}.txt] to check if it exists and it does exist.")
                user_data = input(f"Enter the data you want to the {user_choice}.txt: ")
                with open(user_choice + ".txt", "a") as f:
                    f.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M')}], {user_data}\n")
                logging.info(f"User entered [{user_data}] to add to [{user_choice}.txt] file.")
            else:
                logging.error(f"User entered [{user_choice}.txt] to check if it exists and it doesn't exist.")
                user_option = input(f"Do You Want to create {user_choice}.txt? Only answer in (yes/no): ").capitalize().strip()
                yes_no(user_option,user_choice)
        elif user_input == 2:
            user_choice = input("Enter the name of file of which you want to check data of: ")
            logging.info(f"User chose to check data in the file.")
            if os.path.exists(user_choice + ".txt"):
                if os.path.getsize(user_choice + ".txt") != 0:
                    with open(user_choice + ".txt", "r") as f:
                        content = f.read()
                        print(content)
                    logging.info(f"user read the data from [{user_choice}.txt] successfully.")
                else:
                    logging.error(f"The file User chose was found to be empty.")
            else:
                logging.warning(f"The file user chose didn't exists.")
        elif user_input == 3:
            logging.info(f"User chose to exit.")
            return False
        elif user_input == 4:
            csv_input = input("Enter the file name: ")
            header = ["name", "city", "age"]
            name = input("Enter Your Name: ").strip()
            city = input("Enter the Name of City in which You Live: ").strip()
            age = input("Enter Your Age: ").strip()
            data = {"name" : name, "city" : city, "age" : age}
            logging.info(f"User entered the following details => {data}.")
            if os.path.exists(csv_input + ".csv"):
                if os.path.getsize(csv_input+".csv") == 0:
                    logging.error(f"User chose to enter the data in [{csv_input}.csv] file but the file is empty.")
                    m = True
                else:
                    m = False
                    logging.info(f"User chose to enter the data in [{csv_input}.csv] file which exists.")
            else:
                m = True
                logging.info(f"User chose to enter the data in [{csv_input}.csv] file by creating the file.")
            with open(csv_input + ".csv", "a", newline = "") as f:
                obj = csv.DictWriter(f, fieldnames = header)

                if m:
                    obj.writeheader()
                obj.writerow(data)
        elif user_input == 5:
            csv_view = input("Enter the name of file you want to check: ")
            if os.path.exists(csv_view+".csv"):
                if os.path.getsize(csv_view+".csv") != 0:
                    logging.info(f"User read {csv_view}.csv")
                    with open(csv_view+".csv", "r", newline = "") as f:
                        reader = csv.DictReader(f)
                        for i, r in enumerate(reader,1):
                            print(f"row {i}=> Name : {r['name']} | City : {r['city']} | Age : {r['age']} ")
                else:
                    logging.error(f"User tried to read {csv_view}.csv but it was found to be empty.")
            else:
                logging.error(f"User tried to read {csv_view}.csv but it was found that it doesn't exists.")
    else:
        logging.warning(f"{user_input} was not in options.")

def yes_no(user_option,user_choice):
    while True:
        if user_option == "Yes":
            logging.info(f"User created {user_choice}.")
            with open(user_choice + ".txt", "a") as g:
                pass
            user_input = input(f"What Do You Want to add to the {user_choice}.txt: ").strip()
            logging.info(f"User Entered {user_input} to enter in {user_choice}.txt")
            with open(user_choice + ".txt", "a") as g:
                g.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}], [{user_input}] has been added.\n")
            break
        elif user_option == "No":
            logging.info(f"User chose to go back by selecting no.")
            break
        else:
            logging.warning(f"User entered the wrong option as Only Yes and No are avaliable options!.")
            user_option = input(f"Do You Want to create {user_choice}.txt? Only answer in (yes/no): ").capitalize().strip()

while True:
    window()
    a = check()
    if a == False:
        print('Thank You For Visiting.')
        break
