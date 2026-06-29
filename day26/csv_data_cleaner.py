import pandas as pd
from datetime import datetime
import time
from pathlib import Path

log_file = Path("log.txt")

def log_text(*message: str) -> None:
    with log_file.open("a", encoding = 'utf-8') as file:
        file.write(f"[{datetime.now().strftime('%d/%B/%Y %H:%M:%S')}] : {message}")

def user_name() -> None:
    print("Your Name?")
    full_name = input("Your Reply: ").strip().capitalize().split(' ')
    first_name = full_name[0]
    log_text(f"User Named {first_name} Has Started The Program.")

def file_name() -> None:
    print("Write The File Name Below Which You Want To Clean")
    user_file = input("Your Reply: ")
    if check_file(user_file):
        File_Name = Path(user_file)
        data = pd.read_csv(File_Name)
        cleaned_data(data)

def cleaned_data(data: str) -> None:
    clean_data = data.copy()

def check_file(user_file: str) -> bool:
    if user_file.endswith(".csv"):
        csv_file = Path(user_file)
        if csv_file.is_file() or csv_file.stat().st_size != 0:
            return True
        else:
            print(f"{user_file} Does Not Exists In Your Database or {user_file} Is Empty!")
            return False
    else:
        print("Only .csv File Are Accepted!")
file_name()
