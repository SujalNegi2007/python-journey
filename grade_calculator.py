#Grade Calculator
print("Welcome To the Grade Calculator!\nIt decides what your child gets!\n")
while True:
    option = input("Enter the total marks of the paper: ")
    if option.isdigit():
        option = int(option)
        break
    else:
        print("Invalid Entry!")
while True:
    menu = input("+-------------------------------------------+\n| To Use Normal Grade Calculator: Enter [1] |\n| To Use Asian Grade Calculator : Enter [2] |\n| To Exit Grade Calculator      : Enter [3] |\n+-------------------------------------------+\n")
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:
            User_input = input("Enter the Marks of your Child: ")
            if User_input.isdigit():
                User_input = int(User_input)
                if User_input == option:
                    print(f"Your Child Got {option} out of {option}! It's  A+ Grade")
                elif User_input > option - option*0.10:
                    print(f"Your Child Got {option - option*0.10} out of {option}. It's A Grade")
                elif User_input > option - option*0.20:
                    print(f"Your Child Got {option - option*0.20} out of {option}. It's A- Grade")
                elif User_input > option - option*0.30:
                    print(f"Your Child Got {option - option*0.30} out of {option}. It's B Grade")
                elif User_input > option - option*0.40:
                    print(f"Your Child Got {option - option*0.40} out of {option}. It's C Grade")
                elif User_input > option - option*0.50:
                    print(f"Your Child Got {option - option*0.50} out of {option}. It's D Grade")
                elif User_input > option - option*0.60:
                    print(f"Your Child Got {option - option*0.60} out of {option}. It's E Grade")
                elif User_input > option - option*0.70:
                    print(f"Your Child Got {option - option*0.70} out of {option}. It's F Grade. You have failed")
            else:
                print("Invalid Entry!")
        elif menu == 2:
            User_input = input("Enter the Marks of your Child: ")
            if User_input.isdigit():
                User_input = int(User_input)
                if User_input == option:
                    print(f"Your Child Got {option} out of {option}! It's  A+ Grade. It's Good.")
                elif User_input > option - option*0.10 :
                    print(f"Your Child Got {option - option*0.10} out of {option}. It's A Grade. It's Okay.")
                elif User_input > option - option*0.20:
                    print(f"Your Child Got {option - option*0.20} out of {option}. It's A- Grade. It's Average.")
                elif User_input > option - option*0.30:
                    print(f"Your Child Got {option - option*0.30} out of {option}. It's B Grade. Whaaa...")
                elif User_input > option - option*0.40:
                    print(f"Your Child Got {option - option*0.40} out of {option}. It's C Grade. Emotional Damage.")
                elif User_input > option - option*0.50:
                    print(f"Your Child Got {option - option*0.50} out of {option}. It's D Grade. Who are you?")
                elif User_input > option - option*0.60:
                    print(f"Your Child Got {option - option*0.60} out of {option}. It's E Grade. Slipper")
                elif User_input > option - option*0.70:
                    print(f"Your Child Got {option - option*0.70} out of {option}. It's F Grade. You have failed. No way the screen is getting laggy So bye. Contact the developer!")
        elif menu == 3:
            print("Thank you for using Grade Calculator!")
            break
        else:
            print("Enter b/w 1 to 3 Only!")
    else:
        print("Invalid Entry!")
