import csv
import os
import pandas as pd
import time
import json
from datetime import datetime
if not os.path.exists("config.json") or os.path.getsize("config.json") == 0:
    with open("config.json", "w") as f:
        json.dump({
            "database_file" : "database.csv",
            "log_file" : "log.txt"
        }, f)
with open("config.json", "r") as f:
    config = json.load(f)
DB_file = config["database_file"]
log_file = config["log_file"]
class timer():
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self,*args):
        elapsed = time.time() - self.start
        database(f"Operation took {elapsed:.3f} seconds.")
def database(message):
    with open(log_file,"a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}], {message}\n")
class InvalidMarksError(Exception):
    pass
if not os.path.exists(DB_file):
    with open(DB_file,"w",newline = "") as f:
        obj = csv.writer(f)
        obj.writerow(["name", "marks", "subject"])
if os.path.getsize(DB_file) == 0:
    with open(DB_file,"w") as f:
        obj = csv.writer(f)
        obj.writerow(["name", "marks", "subject"])
def window():
    print("\n\n+------------------------------------------------------+\n| To Add Data Into Database                : Enter [1] |\n| To See The Average Marks of Each Subject : Enter [2] |\n| To See The Highest Scorer                : Enter [3] |\n| To See The Lowest Scorer                 : Enter [4] |\n| To See The Small Portion of Data         : Enter [5] |\n| To View The Whole Database               : Enter [6] |\n| To Exit The System                       : Enter [7] |\n+------------------------------------------------------+\n")
def asking():
    with timer():
        full_name = input("Enter the Name of the Student: ").capitalize().strip()
        a = full_name.split(" ")
        name = a[0]
        while True:
            marks = input("Enter the Marks of the Student: ")
            try:
                if marks.isdigit():
                    marks = int(marks)
                    if 0 <= marks <= 100:
                        break
                    else:
                        raise InvalidMarksError("Given Input Is Outside The Set Range!")
                else:
                    raise ValueError ("Must contain numbers!")
            except Exception as e:
                print(f"Please Enter Valid Input! Error: {e}")
            else:
                print("Marks Saved")
        subject = input("Enter the Subject of the Student: ").capitalize().strip()
        b = [name, marks, subject]
        return b
def yes_no(user_choice):
    with timer():
        while True:
            user_yes_no = input(f"Are You Sure You Want To Enter {user_choice}? Answer by Yes/No: ").capitalize().strip()
            if user_yes_no == "Yes":
                return "Yes"
            elif user_yes_no == "No":
                return "No"
            else:
                print("Only Options Avaliable are Yes/No!")
def checking_int():
    with timer():
        while True:
            user_choice = input("Enter Your Choice: ")
            try:
                user_yes_no = yes_no(user_choice)
                user_choice = int(user_choice)
                if user_yes_no == "Yes":
                    return "yes", user_choice
                elif user_yes_no == "No":
                    print("Going Back...")
                    return "back",user_choice
            except Exception as e:
                print(f"Please Enter Valid Input! Error: {e}")
            else:
                print("Input Taken.")
def assigning_digit():
    user_choice_in_assign_func, user_choice = checking_int()
    if user_choice_in_assign_func != "back":
        if user_choice == 1:
            adding_to_database()
        elif user_choice == 2:
            option_2()
        elif user_choice == 3:
            option_3()
        elif user_choice == 4:
            option_4()
        elif user_choice == 5:
            option_5()
        elif user_choice == 6:
            option_6()
        elif user_choice == 7:
            return "back"
        else:
            print("Only Options are avaliable b/w 1 to 7!")
    else:
        return
def adding_to_database():
    with timer():
        b = asking()
        try:
            with open(DB_file,"a", newline = "") as csv_writer:
                obj = csv.writer(csv_writer)
                obj.writerow(b)
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                obj =csv.writer(csv_writer)
                obj.writerow(b)
        else:
            print("Added to the File.")
        finally:
            print("Operation Complete.")
def option_6():
    with timer():
        try:
            db = pd.read_csv(DB_file)
            if not db.empty:
                print(db)
            else:
                print("There is no data present!")
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        finally:
            print("Operation Complete.")
def option_5():
    with timer():
        try:
            db = pd.read_csv(DB_file)
            if not db.empty:
                print(db.head())
            else:
                print("There is no data present!")
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        finally:
            print("Operation Complete.")
def option_2():
    with timer():
        try:
            db = pd.read_csv(DB_file)
            db['marks'] = pd.to_numeric(db['marks'],errors = "coerce")
            print(db.groupby('subject')['marks'].mean())
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        finally:
            print("Operation Complete.")
def option_3():
    with timer():
        try:
            db = pd.read_csv(DB_file)
            db['marks'] = pd.to_numeric(db['marks'],errors = "coerce")
            clean_db = db.dropna(subset=['marks'])
            print(clean_db.loc[clean_db['marks'].idxmax()])
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        finally:
            print("Operation Complete.")
def option_4():
    with timer():
        try:
            db = pd.read_csv(DB_file)
            db["marks"] = pd.to_numeric(db["marks"],errors = "coerce")
            clean_db = db.dropna(subset=['marks'])
            print(clean_db.loc[clean_db['marks'].idxmin()])
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        finally:
            print("Operation Complete.")
while True:
    window()
    a = assigning_digit()
    if a == "back":
        break
