#Fizzbuzz
print("Welcome to FizzBuzz!")
History = {"Fizz" : [], "Buzz" : [], "FizzBuzz" : []}
while True:
    User_input = input("\n+-----------------------------+\n| To play FizzBuzz: Enter [1] |\n| To view history : Enter [2] |\n| To Clear History: Enter [3] |\n| To Exit         : Enter [4] |\n+-----------------------------+\n")
    try:
        if User_input.isdigit():
            User_input = int(User_input)
            if User_input == 1:
                User_input1 = input("Enter the number from where you want to start the game: ")
                try:
                    if User_input1.isdigit():
                        User_input1 = int(User_input1)
                        User_input2 = input("Enter the number where you want to end the game: ")
                        if User_input2.isdigit():
                            User_input2 = int(User_input2)
                            for i in range(User_input1,User_input2 + 1):
                                if i%3 == 0 and i%5 == 0:
                                    print("FizzBuzz")
                                    History["FizzBuzz"].append(i)
                                elif i%3 == 0:
                                    print("Fizz")
                                    History["Fizz"].append(i)
                                elif i%5 == 0:
                                    print("Buzz")
                                    History["Buzz"].append(i)
                                else:
                                    print(i)
                        else:
                            print("Only Integer are allowed!")
                    else:
                        print("Only Integer are allowed!")
                except:
                    print("Invalid Input! Error: 002")
            elif User_input == 2:
                if any(History.values()):
                    for key, value in dict.items(History):
                        print(f"{key} => {value}")
                else:
                    print("No History Avaliable!")
            elif User_input == 3:
                History.clear()
                History = {"Fizz" : [], "Buzz" : [], "FizzBuzz" : []}
                print("History Cleared Successfully!")
            elif User_input == 4:
                print("Exiting...")
                break
            else:
                print("Only option avaliable are 1 to 4.")
    except:
        print("Invalid Input! Error: 001")
