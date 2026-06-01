import csv
from grade_manager import DB_file
from grade_manager import database
from grade_manager import utils
from grade_manager import display
from pathlib import Path

if not Path(DB_file).exists() or Path(DB_file).stat().st_size == 0:
    with Path(DB_file).open("w") as f:
        obj = csv.writer(f)
        obj.writerow(["name", "marks", "subject"])

def window():
    print("\n\n+------------------------------------------------------+\n| To Add Data Into Database                : Enter [1] |\n| To See The Average Marks of Each Subject : Enter [2] |\n| To See The Highest Scorer                : Enter [3] |\n| To See The Lowest Scorer                 : Enter [4] |\n| To See The Small Portion of Data         : Enter [5] |\n| To View The Whole Database               : Enter [6] |\n| To Exit The System                       : Enter [7] |\n| To repair the file                       : Enter [8] |\n+------------------------------------------------------+\n")
def asking():
    with utils.timer():
        full_name = input("Enter the Name of the Student: ").capitalize().strip()
        a = full_name.split(" ")
        name = a[0]
        while True:
            marks = input("Enter the Marks of the Student: ")
            try:
                marks = int(marks)
                if 0 <= marks <= 100:
                    break
                else:
                    raise utils.InvalidMarksError("Given Input Is Outside The Set Range!")
            except ValueError:
                print("Must contain numbers!")
            except Exception as e:
                print(f"Error: {e}")
        subject = input("Enter the Subject of the Student: ").capitalize().strip()
        b = [name, marks, subject]
        return b
def yes_no(user_choice):
    with utils.timer():
        while True:
            user_yes_no = input(f"Are You Sure You Want To Enter {user_choice}? Answer by Yes/No: ").capitalize().strip()
            if user_yes_no == "Yes":
                return "Yes"
            elif user_yes_no == "No":
                return "No"
            else:
                print("Only Options Avaliable are Yes/No!")
def checking_int():
    with utils.timer():
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
            student = asking()
            database.adding_to_database(student)
        elif user_choice == 2:
            display.option_2()
        elif user_choice == 3:
            display.option_3()
        elif user_choice == 4:
            display.option_4()
        elif user_choice == 5:
            display.option_5()
        elif user_choice == 6:
            display.option_6()
        elif user_choice == 7:
            return "back"
        elif user_choice == 8:
            display.option_8()
        else:
            print("Only Options are avaliable b/w 1 to 8!")
    else:
        return

while True:
    window()
    a = assigning_digit()
    if a == "back":
        break
