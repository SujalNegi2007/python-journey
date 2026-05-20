#Rock Paper Scissor
import random
options = ("Rock", "Paper", "Scissor")
print("Welcome to the Rock-Paper-Scissor Game!")
Full_Name = input("Enter Your Full Name: ").strip().capitalize()
Full_Name = " ".join(w.capitalize() for w in Full_Name.split())
Name = Full_Name.split(" ")
Surname = Name[-1].capitalize()
Main_Name = Name[0]
Your_Overall_Score = 0
print(f"Hello, {Surname}. Nice to meet you.\n")
while True:
    Menu = int(input(f"To play three times: Enter *1*\nTo play five times : Enter *2*\nTo escape the game : Enter *3*\n"))
    
    if Menu == 1:
        Your_score = 0
        Computer_score = 0
        for i in range(3):
            print("\nChoose your options:")
            for number, option in enumerate(options, 1):
                print(f"{number}. {option}")
            Computer_choice = random.choice(options)
            User_choice = input("Enter the name of option your choice: ").capitalize().strip()
            if User_choice == "Rock":
                if Computer_choice == User_choice:
                    print("It's A Tie!")
                elif Computer_choice == "Scissor":
                    print("You Won!")
                    Your_score += 1
                elif Computer_choice == "Paper":
                    print("You Lose!")
                    Computer_score += 1
            elif User_choice == "Paper":
                if Computer_choice == User_choice:
                    print("It's A Tie!")
                elif Computer_choice == "Rock":
                    print("You Won!")
                    Your_score += 1
                elif Computer_choice == "Scissor":
                    print("You Lose!")
                    Computer_score += 1
            elif User_choice == "Scissor":
                if Computer_choice == User_choice:
                    print("It's A Tie!")
                elif Computer_choice == "Paper":
                    print("You Won!")
                    Your_score += 1
                elif Computer_choice == "Rock":
                    print("You Lose!")
                    Computer_score += 1
            else:
                print("Only Rock/Paper/Scissor are allowed.")
        if Your_score > Computer_score:
            print(f"You Won This Match {Main_Name}! By the score of {Your_score} to {Computer_score}")
            Your_Overall_Score += 1
        elif Your_score < Computer_score:
            print(f"You Lost This Match {Main_Name}! By the score of {Your_score} to {Computer_score}")
        else:
            print(f"It's a tie {Main_Name}! By the score of {Your_score} to {Computer_score}")
    elif Menu == 2:
        Your_score = 0
        Computer_score = 0
        for i in range(5):
            print("\nChoose your options:")
            for number, option in enumerate(options, 1):
                print(f"{number}. {option}")
            Computer_choice = random.choice(options)
            User_choice = input("Enter the name of option your choice: ").capitalize().strip()
            if User_choice == "Rock":
                if Computer_choice == User_choice:
                    print("It's A Tie!")
                elif Computer_choice == "Scissor":
                    print("You Won!")
                    Your_score += 1
                elif Computer_choice == "Paper":
                    print("You Lose!")
                    Computer_score += 1
            elif User_choice == "Paper":
                if Computer_choice == User_choice:
                    print("It's A Tie!")
                elif Computer_choice == "Rock":
                    print("You Won!")
                    Your_score += 1
                elif Computer_choice == "Scissor":
                    print("You Lose!")
                    Computer_score += 1
            elif User_choice == "Scissor":
                if Computer_choice == User_choice:
                    print("It's A Tie!")
                elif Computer_choice == "Paper":
                    print("You Won!")
                    Your_score += 1
                elif Computer_choice == "Rock":
                    print("You Lose!")
                    Computer_score += 1
            else:
                print("Only Rock/Paper/Scissor are allowed.")
        if Your_score > Computer_score:
            print(f"You Won This Match {Main_Name}! By the score of {Your_score} to {Computer_score}")
            Your_Overall_Score += 1
        elif Your_score < Computer_score:
            print(f"You Lost This Match {Main_Name}! By the score of {Your_score} to {Computer_score}")
        else:
            print(f"It's a tie {Main_Name}! By the score of {Your_score} to {Computer_score}")
    elif Menu == 3:
        break
    else:
        print("Only 1/2/3 are allowed.")
print(f"Total No. of Matches {Full_Name} have won: {Your_Overall_Score}")
