import csv
import os
import pandas as pd
if not os.path.exists("database.csv"):
    f = open("database.csv","w",newline = "")
    obj = csv.writer(f)
    obj.writerow(["name", "marks", "subject"])
    f.close()
if os.path.getsize('database.csv') == 0:
    f = open("database.csv","w")
    obj = csv.writer(f)
    obj.writerow(["name", "marks", "subject"])
    f.close()
def window():
    print("\n\n+------------------------------------------------------+\n| To Add Data Into Database                : Enter [1] |\n| To See The Average Marks of Each Subject : Enter [2] |\n| To See The Highest Scorer                : Enter [3] |\n| To See The Lowest Scorer                 : Enter [4] |\n| To See The Small Portion of Data         : Enter [5] |\n| To View The Whole Database               : Enter [6] |\n| To Exit The System                       : Enter [7] |\n+------------------------------------------------------+\n")
def asking():
    full_name = input("Enter the Name of the Student: ").capitalize().strip()
    a = full_name.split(" ")
    name = a[0]
    while True:
        marks = input("Enter the Marks of the Student: ")
        if marks.isdigit():
            break
        print("Enter the valid marks!")
    subject = input("Enter the Subject of the Student: ").capitalize().strip()
    b = [name, marks, subject]
    return b
def yes_no(user_choice):
    while True:
        user_yes_no = input(f"Are You Sure You Want To Enter {user_choice}? Answer by Yes/No: ").capitalize().strip()
        if user_yes_no == "Yes":
            return "Yes"
        elif user_yes_no == "No":
            return "No"
        else:
            print("Only Options Avaliable are Yes/No!")
def checking_int():
    while True:
        user_choice = input("Enter Your Choice: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            user_yes_no = yes_no(user_choice)
            if user_yes_no =="Yes":
                return user_choice
            elif user_yes_no =="No":
                print("Going Back...")
                return "back"
        else:
            print("Please Enter Valid Input!")
def assigning_digit():
    user_choice_in_assign_func = checking_int()
    if user_choice_in_assign_func != "back":
        if user_choice_in_assign_func == 1:
            adding_to_database()
        elif user_choice_in_assign_func == 2:
            option_2()
        elif user_choice_in_assign_func == 3:
            option_3()
        elif user_choice_in_assign_func == 4:
            option_4()
        elif user_choice_in_assign_func == 5:
            option_5()
        elif user_choice_in_assign_func == 6:
            option_6()
        elif user_choice_in_assign_func == 7:
            return "back"
        else:
            print("Only Options are avaliable b/w 1 to 7!")
    else:
        return
def adding_to_database():
    b = asking()
    with open("database.csv","a", newline = "") as csv_writer:
        obj = csv.writer(csv_writer)
        obj.writerow(b)
def option_6():
    try:
        db = pd.read_csv('database.csv')
        if not db.empty:
            print(db)
        else:
            print("There is no data present!")
    except Exception as e:
        print(f"Error: {e}!")
def option_5():
    try:
        db = pd.read_csv('database.csv')
        if not db.empty:
            print(db.head())
        else:
            print("There is no data present!")
    except Exception as e:
        print(f"Error: {e}!")
def option_2():
    try:
        db = pd.read_csv('database.csv')
        db['marks'] = pd.to_numeric(db['marks'],errors = "coerce")
        print(db.groupby('subject')['marks'].mean())
    except Exception as e:
        print(f"Error: {e}!")
def option_3():
    try:
        db = pd.read_csv('database.csv')
        db['marks'] = pd.to_numeric(db['marks'],errors = "coerce")
        clean_db = db.dropna(subset=['marks'])
        print(clean_db.loc[clean_db['marks'].idxmax()])
    except Exception as e:
        print(f"Error: {e}!")
def option_4():
    try:
        db = pd.read_csv('database.csv')
        db["marks"] = pd.to_numeric(db["marks"],errors = "coerce")
        clean_db = db.dropna(subset=['marks'])
        print(clean_db.loc[clean_db['marks'].idxmin()])
    except Exception as e:
        print(f"Error: {e}!")
while True:
    window()
    a = assigning_digit()
    if a == "back":
        break
