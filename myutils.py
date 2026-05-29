import os

def name():
    full_name = input("Enter Your Full Name: ")
    full_name = full_name.split(" ")
    first_name = full_name[0]
    return first_name

def yes_no():
    while True:
        user_input = input("Are you sure(yes/no)?").capitalize().strip()
        if user_input == "Yes":
            return "Yes"
        elif user_input == "No":
            return "No"
        else:
            print("Only Yes And No Are Avaliable For Options!")

def check_file(filename_txt):
    if not os.path.exists(filename_txt):
        print(f"{filename_txt} does not exist!\nCreating New One...")
        check = filename_txt.split(".")
        filename_type = check[-1]
        if filename_type == "csv":
            with open(filename_txt,"a",newline="") as csv_reader:
                pass
        elif filename_type == "txt":
            with open(filename_txt,"a") as f:
                pass
        else:
            print("Error: Can't Create This File!")