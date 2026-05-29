#________________________________________________________________________________
Dictionaries = {}
print("Welcome To The Contact Book!\n")
while True:
    Options = int(input("\n+-----------------------------------+\n|To Add contact          : Enter *1*|\n|To Remove contact       : Enter *2*|\n|To Search contact       : Enter *3*|\n|To View all contacts    : Enter *4*|\n|To Update contact number: Enter *5*|\n|To Exit                 : Enter *6*|\n+-----------------------------------+\n"))
#________________________________________________________________________________
    if Options == 1:
        Name = input("\nEnter Your Name: ").capitalize().strip()
        if Name in Dictionaries:
            print(f"Already have {Name}! And its Contact is {Dictionaries[Name]}")
            continue
        Contact = input("Enter the Contact: ")
        if Contact in Dictionaries.values():
            print(f"Already have {Contact}!")
            continue
        Dictionaries[Name] = Contact
#________________________________________________________________________________
    elif Options == 2:
        User_input_delete = input("Enter the Name of the person you want to remove: ").capitalize().strip()
        if User_input_delete in Dictionaries:
            Confirmation = input(f"Are you sure you want to delete the contact of {User_input_delete}: Enter by (Yes/No): ").capitalize().strip()
            if Confirmation == "Yes":
                Dictionaries.pop(User_input_delete)
            elif Confirmation == "No":
                continue
            else:
                Confirmation = input(f"Enter by (Yes/No)").capitalize().strip()
                while True:
                    if Confirmation == "Yes":
                        Dictionaries.pop(User_input_delete)
                        break
                    elif Confirmation == "No":
                        continue
                    else:
                        print("Only yes and no are allowed!")
                        break
        else:
            print("Not found in Database!")
#________________________________________________________________________________
    elif Options == 3:
        User_input_search = input("Enter the Name of person you want to check that exists in database: ").capitalize().strip()
        if User_input_search in Dictionaries.keys():
            print(f"Yes, {User_input_search} exists in the database. And it's Contact is {Dictionaries[User_input_search]}")
        else:
            print(f"No, {User_input_search} does not exist in the database.")
#________________________________________________________________________________
    elif Options == 4:
        for Name, Contact in Dictionaries.items():
            print(f"Name : {Name} -> Contact : {Contact}")
#________________________________________________________________________________
    elif Options == 5:
        User_input_edit = input("Enter the Name of person you want to edit in the database: ").capitalize().strip()
        if User_input_edit in Dictionaries.keys():
            Confirmation = input("Do you want to update the data base?(yes/no): ").capitalize().strip()
            if Confirmation == "Yes":
                Name_Contact = input("Enter what you want to update(Name/Contact): ").capitalize().strip()
#________________________________________________________________________________
                if Name_Contact == "Name":
                    Change_Name = input(f"Enter the Name you want to change with {User_input_edit}: ").capitalize().strip()
                    Old_Name = Dictionaries[User_input_edit]
                    Dictionaries.pop(User_input_edit)
                    Dictionaries.update({
                        Change_Name : Old_Name
                    })
#________________________________________________________________________________
                elif Name_Contact == "Contact":
                    Change_Contact = input(f"Enter the Contact you want to change with {Dictionaries[User_input_edit]}: ")
                    Dictionaries[User_input_edit] = Change_Contact
            elif Confirmation == "No":
                continue
#________________________________________________________________________________
        else:
            print(f"{User_input_edit} is not in Dictionary!")
#________________________________________________________________________________
    elif Options == 6:
        break
#________________________________________________________________________________
