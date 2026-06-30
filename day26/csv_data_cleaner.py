import pandas as pd
from datetime import datetime
from pathlib import Path

log_file = Path("log.txt")

def log_text(message: str) -> None:
    with log_file.open("a", encoding = 'utf-8') as file:
        file.write(f"[{datetime.now().strftime('%d/%B/%Y %H:%M:%S')}] : {message}\n")

def user_name() -> None:
    print("Your Name?")
    full_name = input("Your Reply: ").strip().capitalize().split(' ')
    first_name = full_name[0]
    log_text(f"User Named {first_name} Has Started The Program.")

def file_name() -> None:
    print("Write The File Name Below Which You Want To Clean")
    user_file = input("Your Reply: ")
    if check_file(user_file):
        ans = yes_no('This Is The File You Want To Clean')
        if ans:
            File_Name = Path(user_file)
            data = pd.read_csv(File_Name)
            final_data = cleaned_data(data)
            final_data.to_csv(user_file, index = False, encoding = 'utf-8')
            print("File successfully cleaned and saved back to disk!")
            log_text(f'User Entered File Name To Clean It. File Name: {user_file}')
        else:
            print('Going Back')
            log_text(f'User Entered File Name But Stopped Mid-Way. File Name: {user_file}')


def cleaned_data(data: pd.DataFrame) -> pd.DataFrame:
    cleaning_data = data.copy()
    limit = len(cleaning_data) * 0.5
    col_to_drop = []
    for col in cleaning_data:
        if cleaning_data[col].isnull().sum() >= limit:
            col_to_drop.append(col)
    cleaning_data = cleaning_data.drop(columns = col_to_drop)
    cleaning_data = cleaning_data.drop_duplicates()
    final_data = seprating_data(cleaning_data)
    print(f"Cleaned Data: \n{cleaning_data}\n")
    return final_data

def seprating_data(cleaning_data) -> pd.DataFrame:
    num_col = cleaning_data.select_dtypes(include = ['number']).columns
    for col in num_col:
        cleaning_data[col] = cleaning_data[col].fillna(cleaning_data[col].median())
    obj_col = cleaning_data.select_dtypes(exclude = ['number']).columns
    for col in obj_col:
        cleaning_data[col] = cleaning_data[col].fillna('Unknown')
    print(f"Columns Containing Numbers: \n{num_col}\n")
    print(f"Columns Containing Objects: \n{obj_col}\n")
    return cleaning_data

def check_file(user_file: str) -> bool:
    if user_file.endswith(".csv"):
        csv_file = Path(user_file)
        if csv_file.is_file() and csv_file.stat().st_size != 0:
            return True
        else:
            print(f"{user_file} Does Not Exists In Your Database or {user_file} Is Empty!")
            return False
    else:
        print("Only .csv File Are Accepted!")
        return False

def yes_no(message = " "):
    print(f"Are You Sure{ message}(Yes/No)?")
    while True:
        user_input = input("Your Reply: ").strip().capitalize()
        if user_input in ['Y', 'Yes']:
            return True
        elif user_input in ['N', 'No']:
            return False
        else:
            print("Only Yes And No Are Allowed!")

def window():
    a = 138
    print("+" + "-"*a + "+" + "\n" + 
          "| " + "To Show Clean Data : Enter [1]".center(a-2) + " |" + "\n" +
          "| " + "To Exit            : Enter [2]".center(a-2) + " |" + "\n" +
          "+" + "-"*a + "+" + "\n")

user_name()
while True:
    window()
    try:
        user_input = int(input("Your Reply: "))
        if 1 <= user_input <=2:
            ans = yes_no()
            if ans:
                if user_input == 1:
                    file_name()
                else:
                    print('Exiting...')
                    break
    except Exception as e:
        print(f"Error Found: {e}")
