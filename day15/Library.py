from pathlib import Path
import json
import utils
import random

Warehouse = "Warehouse.json"

class library:

    def Availability(self, Title):
        z = utils.yes_no()
        if z =="True":
            with Path(Warehouse).open("r") as f:
                a = json.load(f)
            if int(a["books"][Title]["available"]) > 0:
                print("Yes, It is available.")
            else:
                print("It is not available.")
        else:
            pass
    
    def borrow(self, Title):
        with Path(Warehouse).open("r") as f:
            a = json.load(f)
        if int(a["books"][Title]["available"]) > 0:
            a["books"][Title]["available"] = int(a["books"][Title]["available"]) - 1
            with Path(Warehouse).open("w") as f:
                json.dump(a, f, indent = 4)
            print("Book Has Been Borrowed.")
        else:
            print("Book is not available.")

    def random_borrow(self):
        with Path(Warehouse).open("r") as f:
            a = json.load(f)
        c = []
        b = list(a["books"].keys())
        for i in range(len(b)):
            if int(a["books"][b[i]]["available"]) > 0:
                c.append(b[i])
        if len(c) != 0:
            d = random.choice(c)
            a["books"][d]["available"] = int(a["books"][d]["available"]) - 1
            with Path(Warehouse).open("w") as f:
                json.dump(a, f, indent = 4)
            print(f"{d} has been borrowed.")
            return d
        else:
            print("Sorry, there are no books available.")

    def borrower(self,h,first_name):
        with Path(Warehouse).open("r") as f:
            a = json.load(f)
        a["members"].setdefault(first_name, {"borrowed" : []})
        a["members"][first_name]["borrowed"].append(h)
        with Path(Warehouse).open("w") as f:
            json.dump(a,f,indent = 4)

    def returned_book(self,first_name):
        with Path(Warehouse).open("r") as f:
            a = json.load(f)
        if first_name in a["members"].keys():
            if len(a["members"][first_name]["borrowed"]) != 0:
                print(f"Books that you have borrowed are: {a["members"][first_name]["borrowed"]}")
                d = utils.yes_no()
                if d == "True":
                    return_book = input("Enter The Name of the book you want to return: ")
                    if return_book in a["members"][first_name]["borrowed"]:
                        a["members"][first_name]["borrowed"].remove(return_book)
                        a["books"][return_book]["available"] = int(a["books"][return_book]["available"]) + 1
                        with Path(Warehouse).open("w") as f:
                            json.dump(a,f,indent = 4)
                    else:
                        print("You don't have this book.")
                else:
                    pass
            else:
                print("You have not borrowed anything.")
        else:
            print("You are not registered in our database.")

    def check_self(self):
        with Path(Warehouse).open("r") as f:
            a = json.load(f)
        for key, value in a["books"].items():
            print(f"{key}    =>    {value}")

with Path(Warehouse).open("r") as f:
    m = json.load(f)
while True:
    first_name = utils.name()
    while True:
        utils.window()
        try:
            user_value = int(input("Your Reply: "))
            if user_value == 1:
                user_borrow = input("Enter the book name that you want to borrow: ")
                if user_borrow in m["books"].keys():
                    user_choice = utils.yes_no()
                    if user_choice == "True":
                        library().borrow(user_borrow)
                        library().borrower(user_borrow, first_name)
                    else:
                        print("Going Back...")
                else:
                    print("This book is not in our store")
            elif user_value == 2:
                book_available = input("Enter the book name that you want to check is available or not: ")
                if book_available in m["books"].keys():
                    user_choice_available = utils.yes_no()
                    if user_choice_available == "True":
                        library().Availability(book_available)
                    else:
                        print("Going Back...")
                else:
                    print("This book is not in our store")
            elif user_value == 3:
                user_choice_random = utils.yes_no()
                if user_choice_random == "True":
                    try:
                        d = library().random_borrow()
                        library().borrower(d, first_name)
                    except Exception as e:
                        print(f"Error: {e}. There could be no books available")
                else:
                    print("Going Back...")
            elif user_value == 4:
                library().returned_book(first_name)
            elif user_value == 5:
                library().check_self()
            elif user_value == 6:
                break
            else:
                print("Invalid Input!")
        except Exception as e:
            print(f"Error: {e}")
