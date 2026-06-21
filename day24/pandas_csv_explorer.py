import pandas as pd
from pathlib import Path
from datetime import datetime
#===============================================================================================================
file_name = Path("student.csv")
log_name = Path("log.txt")
#===============================================================================================================
def log_entry(message):
    with log_name.open("a", encoding = "utf-8") as log:
        log.write(f"[{datetime.now().strftime('%d/%B/%Y %H:%M:%S')}]: {message}\n")

def name():
    print("\nYour Name?")
    full_name = input("Your Reply: ").strip().capitalize()
    full_name = full_name.split(" ")
    first_name = full_name[0]
    last_name = full_name[-1]
    if first_name == last_name:
        log_entry(f"User Entered His Name. Name -> {first_name}.")
        return first_name
    else:
        log_entry(f"User Entered His Name. First Name -> {first_name}  Last Name -> {last_name}.")
        return first_name

def yes_no(message = ""):
    print(f"Are You Sure{ message}(Yes/No)?")
    while True:
        user_input = input("Your Reply: ").strip().capitalize()
        if user_input in ["Y", "Yes"]:
            return True
        elif user_input in ["N", "No"]:
            return False
        else:
            print("Only Yes And No Are Available.")

def window():
    a = 138
    print("+" + "-"*a + "+" + "\n" +
          "| " + "To Check Whole Database                  : Enter [1]".center(a-2) + " |" + "\n"#info
          "| " + "To Check The Database containing Numbers : Enter [2]".center(a-2) + " |" + "\n"#describe
          "| " + "To Check Size of Database                : Enter [3]".center(a-2) + " |" + "\n"#shape
          "| " + "To Check The Data Type of each column    : Enter [4]".center(a-2) + " |" + "\n"#dtype
          "| " + "To Check Total NaN values of each column : Enter [5]".center(a-2) + " |" + "\n"#isnull().sum()
          "| " + "To Exit                                  : Enter [6]".center(a-2) + " |" + "\n"#to escape
          "+" + "-"*a + "+" + "\n"
          )

user_name = name()
while True:
    if not file_name.is_file() or file_name.stat().st_size == 0:
        print("\nError: File Not Found Or File is Empty!\n")
        break
    else:
        with file_name.open("r", encoding = "utf-8") as file:
            data = pd.read_csv(file)
    window()
    try:
        menu_option = int(input("Your Reply: "))
        if 1 <= menu_option <= 6:
            ans = yes_no(f"you want to choose {menu_option}?")
            if ans:
                if menu_option == 1:
                    print(data.info())
                elif menu_option == 2:
                    print(data.describe())
                elif menu_option == 3:
                    print(f"The Size of data is {data.shape}")
                elif menu_option == 4:
                    print("Data type of Each Column are: ")
                    print(data.dtypes())
                elif menu_option == 5:
                    print("Total NaN values of each column are: ")
                    print(data.isnull().sum())
                else:
                    print("Thanks for Using This Code!\nExiting...")
                    break
            else:
                print("Exiting...")
        else:
            print("Only b/w 1 to 6 options are currently available.")
    except ValueError:
        print("Only b/w 1 to 6 options are currently available.")
