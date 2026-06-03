from pathlib import Path
import json
import utils
import random
import csv
import book_types

Warehouse = "Warehouse.json"

class library:

    def __init__(self):
        with Path(Warehouse).open("r") as f:
            self.a = json.load(f)
    
    def save(self):
        with Path(Warehouse).open("w") as f:
            json.dump(self.a, f, indent = 4)

    def Availability(self, Title):
        z = utils.yes_no()
        if z =="True":
            if int(self.a["books"][Title]["available"]) > 0:
                print("Yes, It is available.")
            else:
                print("It is not available.")
        else:
            pass
    
    def borrow(self, Title):
        if int(self.a["books"][Title]["available"]) > 0:
            self.a["books"][Title]["available"] = int(self.a["books"][Title]["available"]) - 1
            self.save()
            print("Book Has Been Borrowed.")
        else:
            print("Book is not available.")

    def random_borrow(self):
        c = []
        b = list(self.a["books"].keys())
        for i in range(len(b)):
            if int(self.a["books"][b[i]]["available"]) > 0:
                c.append(b[i])
        if len(c) != 0:
            d = random.choice(c)
            self.a["books"][d]["available"] = int(self.a["books"][d]["available"]) - 1
            self.save()
            print(f"{d} has been borrowed.")
            return d
        else:
            print("Sorry, there are no books available.")

    def borrower(self,h,first_name):
        self.a["members"].setdefault(first_name, {"borrowed" : []})
        self.a["members"][first_name]["borrowed"].append(h)
        self.save()

    def returned_book(self,first_name):
        if first_name in self.a["members"].keys():
            if len(self.a["members"][first_name]["borrowed"]) != 0:
                print(f"Books that you have borrowed are: {self.a['members'][first_name]['borrowed']}")
                d = utils.yes_no()
                if d == "True":
                    return_book = input("Enter The Name of the book you want to return: ")
                    if return_book in self.a["members"][first_name]["borrowed"]:
                        self.a["members"][first_name]["borrowed"].remove(return_book)
                        self.a["books"][return_book]["available"] = int(self.a["books"][return_book]["available"]) + 1
                        self.save()
                    else:
                        print("You don't have this book.")
                else:
                    pass
            else:
                print("You have not borrowed anything.")
        else:
            print("You are not registered in our database.")

    def check_self(self):
        for key, value in self.a["books"].items():
            print(f"{key}    =>    {value}")
    
    def check_author(self, author):
        b = list(self.a["books"].keys())
        c = []
        for i in range(len(b)):
            if self.a["books"][b[i]]["author"] == author:
                c.append(b[i])
        if len(c) != 0:
            print(f"All Books Written By {author} are: ")
            for i in range(len(c)):
                print(f"Book {i + 1} => {c[i]}")
        else:
            print(f"There are no books available in the library whose author is {author}.")

    def all_available_books(self):
        b = list(self.a["books"].keys())
        c = []
        for i in range(len(b)):
            if int(self.a["books"][b[i]]["available"]) > 0:
                c.append(b[i])
        if len(c) != 0:
            print("Available books are: ")
            for i in range(len(c)):
                print(f"Book {i+1} => {c[i]}")
        else:
            print("There are no available books.")
    
    def changing_to_csv(self):
        field = ["Books", "Author", "Available", "Pages", "Duration_mins", "File_size_mb", "Type"]
        b = list(self.a["books"].keys())
        d = []
        for i in range(len(b)):
            c = {}
            c["Books"] = b[i]
            c["Author"] = self.a["books"][b[i]]["author"]
            c["Available"] = self.a["books"][b[i]]["available"]
            c["Pages"] = self.a["books"][b[i]].get("pages", "N/A")
            c["Duration_mins"] = self.a["books"][b[i]].get("duration_mins", "N/A")
            c["File_size_mb"] = self.a["books"][b[i]].get("file_size_mb", "N/A")
            c["Type"] = self.a["books"][b[i]]["type"]
            d.append(c)
        with Path("Warehouse.csv").open("w") as f:
            obj = csv.DictWriter(f, fieldnames = field)
            obj.writeheader()
            obj.writerows(d)
        
    def changing_to_json(self):
        a = {"books":{}, "members": {}}
        with Path("Warehouse.csv").open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = row["Books"]
                q = row["Author"]
                r = row["Available"]
                s = row["Pages"]
                u = row["Duration_mins"]
                v = row["File_size_mb"]
                w = row["Type"]
                try:
                    r = int(r)
                except:
                    pass
                try:
                    s = int(s)
                except:
                    pass
                try:
                    u = int(u)
                except:
                    pass
                try:
                    v = float(v)
                except:
                    pass
                w = row["Type"]
                a["books"][p] = {"available" : r, "author" : q, "pages" : s, "duration_mins" : u, "file_size_mb" : v, "type" : w}
        with Path("Warehouse.json").open("w") as f:
            json.dump(a,f,indent = 4)
    def display_clean_data(self):
        b = list(self.a["books"].keys())
        for i in range(len(b)):
            if self.a["books"][b[i]]["type"] == "book":
                book_types.book(self.a["books"][b[i]]["author"], self.a["books"][b[i]]["available"], b[i], self.a["books"][b[i]]["pages"]).display_info()
            elif self.a["books"][b[i]]["type"] == "ebook":
                book_types.ebook(self.a["books"][b[i]]["author"], self.a["books"][b[i]]["available"], b[i], self.a["books"][b[i]]["pages"], self.a["books"][b[i]]["file_size_mb"]).display_info()
            elif self.a["books"][b[i]]["type"] == "audiobook":
                book_types.audiobook(self.a["books"][b[i]]["author"], self.a["books"][b[i]]["available"], b[i], self.a["books"][b[i]]["file_size_mb"], self.a["books"][b[i]]["duration_mins"]).display_info()


lib = library()


while True:
    first_name = utils.name()
    while True:
        utils.window()
        try:
            user_value = int(input("Your Reply: "))
            if user_value == 1:
                user_borrow = input("Enter the book name that you want to borrow: ")
                if user_borrow in lib.a["books"].keys():
                    user_choice = utils.yes_no()
                    if user_choice == "True":
                        lib.borrow(user_borrow)
                        lib.borrower(user_borrow, first_name)
                    else:
                        print("Going Back...")
                else:
                    print("This book is not in our store")
            elif user_value == 2:
                book_available = input("Enter the book name that you want to check is available or not: ")
                if book_available in lib.a["books"].keys():
                    lib.Availability(book_available)
                else:
                    print("This book is not in our store")
            elif user_value == 3:
                user_choice_random = utils.yes_no()
                if user_choice_random == "True":
                    try:
                        d = lib.random_borrow()
                        lib.borrower(d, first_name)
                    except Exception as e:
                        print(f"Error: {e}. There could be no books available")
                else:
                    print("Going Back...")
            elif user_value == 4:
                lib.returned_book(first_name)
            elif user_value == 5:
                lib.display_clean_data()
            elif user_value == 6:
                author = input("Enter the name of author: ")
                lib.check_author(author)
            elif user_value == 7:
                lib.all_available_books()
            elif user_value == 8:
                lib.check_self()
            elif user_value == 9:
                lib.changing_to_csv()
            elif user_value == 10:
                lib.changing_to_json()
            elif user_value == 11:
                break
            else:
                print("Invalid Input!")
        except Exception as e:
            print(f"Error: {e}")
