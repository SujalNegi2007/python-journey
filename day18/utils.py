def yes_no():
    print("Are You Sure(yes/no)?")
    while True:
        user_input = input("Your Reply: ").capitalize().strip()
        if user_input == "Yes":
            print("...")
            return "True"
        elif user_input == "No":
            print("Going Back...")
            return "False"
        else:
            print("Only Yes And No Are Avaliable!")

def window():
    print("\n+------------------------------------------------------------+\n| To Borrow A Book                               : Enter [1] |\n| To Check If A Book Is Avaliable                : Enter [2] |\n| Want To Borrow A Random Book                   : Enter [3] |\n| Want To Return A Book                          : Enter [4] |\n| To Check Shelf                                 : Enter [5] |\n| To Search Book By Author's Name                : Enter [6] |\n| To check all available books                   : Enter [7] |\n| To Check Raw Data                              : Enter [8] |\n| To Convert The Json Database Into CSV Database : Enter [9] |\n| To Convert CSV into json                      : Enter [10] |\n| To Exit The Library                           : Enter [11] |\n| To Display Books By Pages                     : Enter [12] |\n+------------------------------------------------------------+\n")

def name():
    user_name = input("\nEnter Your Name: ").capitalize().strip()
    split_name = user_name.split(" ")
    first_name = split_name[0]
    return first_name
