import numpy as np

cities = 20
random_number = np.random.default_rng(seed = 1)

temperature = random_number.integers(-10,46, size = cities)
rain_chance = random_number.integers(1,100, size = cities)
city_name = [
    "Tokyo", "Delhi", "Shanghai", "New York", "Mumbai", 
    "London", "Paris", "Dubai", "Singapore", "Sydney", 
    "Cairo", "Toronto", "Seoul", "Bangkok", "Berlin", 
    "Moscow", "Rome", "Cape Town", "Chicago", "Los Angeles"
]

def yes_no()->bool:
    print("Are You Sure(Yes/No)?")
    while True:
        user_yes_no = input("Your Reply: ")
        if user_yes_no == "Yes":
            return True
        elif user_yes_no == "No":
            return False
        else:
            print("Only Yes And No Are Available!")

times = 68

def menu_screen():
    print("+" + "-"*times + "+" + "\n" +
          "|" + "To Check The Hottest City                    : Enter [1]".center(times) + "|" + "\n" +
          "|" + "To Check The Coldest City                    : Enter [2]".center(times) + "|" + "\n" +
          "|" + "To Check The City With Highest Rain Chance   : Enter [3]".center(times) + "|" + "\n" +
          "|" + "To Check The City With Lowest Rain Chance    : Enter [4]".center(times) + "|" + "\n" +
          "|" + "To Check The Average Temperature Of The City : Enter [5]".center(times) + "|" + "\n" +
          "|" + "To Check The Average rain_chance Of The City : Enter [6]".center(times) + "|" + "\n" +
          "|" + "To Check The City That Are In Danger Zone    : Enter [7]".center(times) + "|" + "\n" +
          "|" + "To Exit The System                           : Enter [8]".center(times) + "|" + "\n" +
          "+" + "-"*times + "+" + "\n")

while True:
    menu_screen()
    try:
        user_input = int(input("Your Reply: "))
        if 1 <= user_input <= 8:
            if user_input == 1:
                i = np.argmax(temperature)
                print("+" + "-"*times + "+" + "\n" +
                      "|" + f"{city_name[i]}'s Temperature          : {temperature[i]}°C ".center(times) + "|" + "\n" +
                      "|" + f"{city_name[i]}'s Rain Chance          : {rain_chance[i]}%  ".center(times) + "|" + "\n" +
                      "+" + "-"*times + "+" + "\n")
            elif user_input == 2:
                i = np.argmin(temperature)
                print("+" + "-"*times + "+" + "\n" +
                      "|" + f"{city_name[i]}'s Temperature          : {temperature[i]}°C ".center(times) + "|" + "\n" +
                      "|" + f"{city_name[i]}'s Rain Chance          : {rain_chance[i]}%  ".center(times) + "|" + "\n" +
                      "+" + "-"*times + "+" + "\n")
            elif user_input == 3:
                i = np.argmax(rain_chance)
                print("+" + "-"*times + "+" + "\n" +
                      "|" + f"{city_name[i]}'s Temperature          : {temperature[i]}°C ".center(times) + "|" + "\n" +
                      "|" + f"{city_name[i]}'s Rain Chance          : {rain_chance[i]}%  ".center(times) + "|" + "\n" +
                      "+" + "-"*times + "+" + "\n")
            elif user_input == 4:
                i = np.argmin(rain_chance)
                print("+" + "-"*times + "+" + "\n" +
                      "|" + f"{city_name[i]}'s Temperature          : {temperature[i]}°C ".center(times) + "|" + "\n" +
                      "|" + f"{city_name[i]}'s Rain Chance          : {rain_chance[i]}%  ".center(times) + "|" + "\n" +
                      "+" + "-"*times + "+" + "\n")
            elif user_input == 5:
                print(f"Average Temperature Of Cities: {np.mean(temperature)}")
            elif user_input == 6:
                print(f"Average Rain Fall Of Cities: {np.mean(rain_chance)}")
            elif user_input == 7:
                danger_normal = np.where((temperature > 40) | (temperature < 5), "Danger Zone", "Normal Zone")
                for i in range(cities):
                    print("+" + "-"*times + "+" + "\n" +
                          "|" + f"{city_name[i]}'s Temperature          : {temperature[i]}°C ".center(times) + "|" + "\n" +
                          "|" + f"{city_name[i]}'s Rain Chance          : {rain_chance[i]}%  ".center(times) + "|" + "\n" +
                          "|" + f"{city_name[i]}'s Zone Type            : {danger_normal[i]} ".center(times) + "|" + "\n" +
                          "+" + "-"*times + "+" + "\n") 
            else:
                print("Thank You For Visiting.")
        else:
            print("Only Options are b/w 1 to 8.")
    except ValueError:
        print("Only Integers Are Allowed")
