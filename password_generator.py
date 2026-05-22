# Password Generator
import random
import string
print("Welcome to the password Generator!")
History = []
#-------------------------------------------------------------------------------------------
while True:
    try:
        menu = int(input("\n+--------------------------------------+\n| To Generate Password     : Enter [1] |\n| To View Password History : Enter [2] |\n| To Exit                  : Enter [3] |\n+--------------------------------------+\n"))
#-------------------------------------------------------------------------------------------
        if menu == 1:
            pool = ""
            password = []
            characters = []
#-------------------------------------------------------------------------------------------
            try:
#-------------------------------------------------------------------------------------------
                while True:
                    uppercase_type = input("\nDo you want to include Uppercase letters for password generation(yes/no)?\n").capitalize().strip()
                    if uppercase_type == "Yes":
                        pool += string.ascii_uppercase
                        print("The Uppercase letters has been added for password generation!\n")
                        break
                    elif uppercase_type == "No":
                        print("The Uppercase letters has not been added for password generation!\n")
                        break
                    else:
                        print("Only Yes and no are available")
#-------------------------------------------------------------------------------------------
                while True:
                    lowercase_type = input("Do you want to include Lowercase letters for password generation(yes/no)?\n").capitalize().strip()
                    if lowercase_type == "Yes":
                        pool += string.ascii_lowercase
                        print("The Lowercase letters has been added for password generation!\n")
                        break
                    elif lowercase_type == "No":
                        print("The Lowercase letters has not been added for password generation!\n")
                        break
                    else:
                        print("Only Yes and no are available")
#-------------------------------------------------------------------------------------------
                while True:
                    number_type = input("Do you want to include Numbers(0-9) for password generation(yes/no)?\n").capitalize().strip()
                    if number_type == "Yes":
                        pool += string.digits
                        print("The Numbers has been added for password generation!\n")
                        break
                    elif number_type == "No":
                        print("The Numbers has not been added for password generation!\n")
                        break
                    else:
                        print("Only Yes and no are available")
#-------------------------------------------------------------------------------------------
                while True:
                    special_type = input("Do you want to include Special for password generation(yes/no)?\n").capitalize().strip()
                    if special_type == "Yes":
                        pool += string.punctuation
                        print("The Special Characters has been added for password generation!\n")
                        break
                    elif special_type == "No":
                        print("The Special Characters has not been added for password generation!\n")
                        break
                    else:
                        print("Only Yes and no are available")
#-------------------------------------------------------------------------------------------
                password_len = int(input("What Should Be The Length of Password: "))
                if uppercase_type == "Yes" or lowercase_type == "Yes" or number_type == "Yes" or special_type == "Yes" and password_len != 0:
                    for i in range(password_len):
                        characters.append(random.choice(pool))
                    random.shuffle(characters)
                    password = "".join(characters)
                    History.append(password)
                else:
                    print("You didn't choose any options to make password! The password is not created!")
#-------------------------------------------------------------------------------------------
            except:
                print("Invalid Input!")
        elif menu == 2:
            print("Loading resources...\nLoading resources...\nLoading resources...")
            print("Presenting the password histories...")
            for i in History:
                print(f"Password =>{i} ")
        elif menu == 3:
            print("Exiting...")
            break
        else:
            print("Invalid Input! Error: 002")
    except:
        print("Invalid Input! Error:001")
