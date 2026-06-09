from pathlib import Path
import csv

def lazy_file_reader(file_path: Path):
    with file_path.open("r", encoding = "utf-8") as file:
        for line in file:
            yield line.strip()

def yes_no():
    print("Are you sure?\n")
    while True:
        user_choice = input("Your Reply: ").capitalize().strip()
        if user_choice == "Yes":
            return True
        elif user_choice == "No":
            return False
        else:
            print("Only Yes and No are available!")

while True:
    try:
        print("If You Want To Exit: Enter [Exit]")
        user_exit = input("Your Reply: ").capitalize().strip()
        if user_exit != "Exit":
            user_input = input("\nEnter the name of the file: ")
            db_file = Path(user_input)
            if db_file.is_file():
                gen =  lazy_file_reader(db_file)
                user_choice = yes_no()
                if user_choice:
                    a = 0
                    print("\n"+"="*50)
                    for line in gen:
                        a += 1
                        if "Error" in line or "Exception" in line:
                            print(f"Possible error detected in line: {a}")
                    print("Operation completed.")
                    print("="*50+"\n")
                    break
                else:
                    print("\n"+"X"*50)
                    print("Operation Cancelled".center(50))
                    print("X"*50 + "\n")
                    break
            else:
                print("\n"+"X"*50)
                print("This file doesn't exists!".center(50))
                print("X"*50 + "\n")
        else:
            print("\n"+"="*50)
            print("Thank you for using our code.".center(50))
            print("="*50+"\n")
            break
        
    except FileNotFoundError:
        print("\n"+"X"*50)
        print("File Not Found!".center(50))
        print("X"*50 + "\n")
