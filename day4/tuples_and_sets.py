#==================== Tuple ====================
Tuple = ("Apple","Banana", "Mango")
while True:
    User_input = input("Enter the tuple you want to add: ").capitalize()
    New_Tuple = Tuple + (User_input,)
    Sorted_Tuple = sorted(New_Tuple)
    Longest_word = max(New_Tuple, key=len)
    Shortest_word = min(New_Tuple, key=len)
    
    check = input("Do you want to check if your word exists in Tuple?\nIf yes Enter *yes*, if not then Enter *No*: ").capitalize()
    if check == "Yes":
        User_input2 = input("Enter the word you want to check: ").capitalize()
        if User_input2 in New_Tuple:
            print(f"Yes, {User_input2} is present in Tuple.")
        else:
            print("Not Found!")

    print(f"Original Tuple     : {Tuple}")
    print(f"New Tuple          : {New_Tuple}")
    print(f"Length of new Tuple: {len(New_Tuple)}")
    print(f"Sorted Tuple       : {Sorted_Tuple}")
    print(f"Longest Word       : {Longest_word}")
    print(f"Shortest Word      : {Shortest_word}")
    Tuple = New_Tuple
    User_input3 = input("If you want to escape Enter *escape*, to continue Enter *Yes*: ").capitalize()
    if User_input3 == "Escape":
        break
#==================== Set ====================
#set analyser and duplication detector
print("Welcome to Set Analyser")
Set = set()
while True:
    User_input = int(input("\nTo add a item into the Set          : Enter *1*\nTo remove a item from the Set       : Enter *2*\nTo escape from menu                 : Enter *3*\nTo check if a item exists in the Set: Enter *4*\nTo view the Set                     : Enter *5*\n"))
    if User_input == 1:
        Set_input = input("Enter the word you want to add in the set: ").capitalize()
        if Set_input in Set:
            print(f"{Set_input} already exists! Duplication is not allowed!")
        else:
            Set.add(Set_input)
            print(f"{Set_input} has been added to the Set.")
    elif User_input == 2:
        if len(Set) == 0:
            print("Set is empty!")
        else:
            Set_input = input("Enter the word you want to remove from the set: ").capitalize()
            Set.discard(Set_input)
            print(f"{Set_input} has been removed from the Set.")
    elif User_input == 3:
        break
    elif User_input == 4:
        Set_input = input("Enter the word you want to check that exists in the set or not: ").capitalize()
        if Set_input in Set:
            print(f"{Set_input} is present in Set.")
        else:
            User_input = input(f"{Set_input} is not present in Set, but you can add it by Enter *add* or can skip it by entering any other button.\n").capitalize()
            if User_input == "Add":
                Set.add(Set_input)
                print(f"{Set_input} has been added to the Set.")
    elif User_input == 5:
        for number, items in enumerate(Set,1):
            print(f"{number}. {items}")
