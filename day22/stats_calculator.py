import numpy as np
from datetime import datetime
from pathlib import Path

file_path = Path("Log.txt")

def log_action(z: str)->None:
    with file_path.open("a") as f:
        f.write(f"[{datetime.now().strftime('%d/%B/%Y %H:%M:%S')}]: {z}.\n")

if not file_path.is_file():
    log_action("Log File Created")

def yes_no()->bool:
    print("Are You Sure?(Yes/No)")
    while True:
        user_yes_no = input("Your Reply: ").strip().capitalize()
        if user_yes_no == "Yes":
            print("Continuing the Operations...\n")
            return True
        elif user_yes_no == "No":
            print("Halting The Operations...\n")
            return False
        else:
            print("Only Yes And No Are Available!")

def show_menu()->None:
    print("+" + "-"*138 + "+" + "\n" +
          "|" +"To Get The Average Of Student : Enter [1]".center(138) + "|" + "\n" +
          "|" +"To Get The Average Of Subject : Enter [2]".center(138) + "|" + "\n" +
          "|" +"To Get The Highest Score      : Enter [3]".center(138) + "|" + "\n" +
          "|" +"To Get The Lowest Score       : Enter [4]".center(138) + "|" + "\n" +
          "|" +"To Exit                       : Enter [5]".center(138) + "|" + "\n" +
          "+" + "-"*138 + "+" + "\n"
          )

data = np.array([
    [85, 65, 75],
    [95, 35, 85],
    [84, 54, 67],
    [85, 65, 98]
])

while True:
    show_menu()
    try:
        user_input = int(input("Your Reply: "))
        if not 1 <= user_input <= 5:
            print("Only options available are b/w 1 to 5.")
        else:
            if yes_no():
                if user_input == 1:
                    print(f"The Average Of Students: {np.mean(data, axis = 1)}\n")
                    log_action("User Chose Option 1 and saw the average of students")
                elif user_input == 2:
                    print(f"The Average Of Subject: {np.mean(data, axis = 0)}\n")
                    log_action("User Chose Option 2 and saw the average of subjects")
                elif user_input == 3:
                    print(f"The Highest Score: {np.max(data)}\n")
                    log_action("User Chose Option 3 and saw the highest score")
                elif user_input == 4:
                    print(f"The Lowest Score: {np.min(data)}\n")
                    log_action("User Chose Option 4 and saw the lowest score")
                elif user_input == 5:
                    print("Exiting...\n")
                    log_action("User Chose Option 5 and exited the system")
                    break
    except ValueError:
        print("Only Integers are allowed!")
