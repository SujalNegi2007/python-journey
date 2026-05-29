#Your Grocery Manager
print("Welcome to the Your Grocery Manager")
print("Here you can add, remove and update things for your cart to keep update of your daily life.")

Grocery_List = []
while True:
    print("\nTo add Grocery          : Enter *1*\nTo remove Grocery       : Enter *2*\nTo Exit the Grocery list: Enter *3*\nTo view Grocery         : Enter *4*\nTo Check if item Exists : Enter *5*")
    option_taken = int(input("\nEnter The Number: "))
    if option_taken == 1:
        Grocery = input("Enter the Grocery that you want to add to the list: ").capitalize().strip()
        Grocery_List.append(Grocery)
    elif option_taken == 2:
        Grocery = input("Enter the Grocery that you want to remove from the list: ").capitalize().strip()
        if Grocery in Grocery_List:
            Grocery_List.remove(Grocery)
        else:
            print("It is not in Grocery List.")
    elif option_taken == 3:
        break
    elif option_taken == 4:
        Grocery_List.sort()
        if len(Grocery_List) >0:
            for Grocery_number, Grocery_items in enumerate(Grocery_List, 1):
                print(f"{Grocery_number}. {Grocery_items}")
        elif len(Grocery_List) == 0:
            print("Your cart is empty! Try entering *1* to add product to your cart.")
        else:
            print("Some technical errors! Try contacting developer for assistance.")
    elif option_taken == 5:
        Grocery = input("Enter the Grocery that you want to check that exists in the list or not: ").capitalize().strip()
        if Grocery in Grocery_List:
            print("Yes, it's already in the cart.")
        else:
            print("It's not in the cart, but you can Enter *add* to add it or press Enter to go back to menu.")
            add_or_menu = input().capitalize().strip()
            if add_or_menu == "Add":
                Grocery_List.append(Grocery)
print("Thanks for using Your Grocery Manager!")
