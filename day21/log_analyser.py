from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime


def file_read(file_path: Path):
    with file_path.open("r", encoding = "utf-8") as f:
        for line in f:
            yield line.strip()

def process_line(line: str,a: int,hits: list,urls_in_hour: dict) -> None:
    url = line.split('"')[1].split('"')[0].split(" ")[1]
    hits.append(url)
    urls_in_hour[f"Hour_{a}"].append(url)

def window()->None:
    print("\n"+"="*140+"\n" +
        "To Enter The File Name : Enter [1]".center(140)+"\n" +
        "To Exit                : Enter [2]".center(140)+"\n" +
        "="*140+"\n")

def yes_no()->bool:
    print("Are You Sure(Yes/No)?")
    while True:
        user_yes_no = input("Your Reply: ").strip().capitalize()
        if user_yes_no == "Yes":
            print("Proceding Operations...")
            return True
        elif user_yes_no == "No":
            print("Halting Operations...")
            return False
        else:
            print("Only yes and no are available.")

while True:
    window()
    try:
        ans = int(input("Your Reply: "))
        if ans == 1:
            server = input("Enter the Name of the File: ")
            server_ans = yes_no()
            if server_ans:
                file_path = Path(server)
                urls_in_hour = defaultdict(list)
                hits = []
                for line in file_read(file_path):
                    try:
                        time_line = line.split("[")[1].split("]")[0]
                        dt_time = datetime.strptime(time_line, '%d/%b/%Y %H:%M:%S')
                        a = dt_time.hour
                        process_line(line,a,hits,urls_in_hour)
                    except (ValueError, IndexError):
                        continue
                url_count = Counter(hits)
                print(url_count.most_common(3))
                for key, value in urls_in_hour.items():
                    print(f"{key} => {value}")
                print("Operation Complete.")
        elif ans == 2:
            print("Thanks for using our code.")
            break
        else:
            print("Only One And Two Are Available")
    except Exception as e:
        print(f"Error Occured: {e}")
