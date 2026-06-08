import csv
from pathlib import Path
db_file = Path("database.csv")
def generator(file_path: Path):
    with file_path.open("r", encoding = "utf-8") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            yield row
gen = generator(db_file)

def window():
    print("\n+---------------------------------------+"
          "\n| If You Want To Read Row : Enter [Yes] |"
          "\n| If You Want To Exit     : Enter [No]  |"
          "\n+---------------------------------------+\n")

def yes_no():
    while True:
        window()
        user_input = input("Your Reply: ").capitalize().strip()
        if user_input == "Yes":
            return True
        elif user_input == "No":
            return False
        else:
            print("Only Yes And No Avaliable For Options!")

while True:
    result = yes_no()
    if result:
        try:
            row_data = next(gen)
            for a, b  in row_data.items():
                print(f"{a} => {b}")
        except StopIteration:
            print(f"You Have Reached The End Of CSV file!")
    else:
        print("Thank You For Using This Code!")
        break
