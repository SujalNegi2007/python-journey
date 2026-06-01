from grade_manager import DB_file
import csv
from grade_manager import utils

def repair_file():
    a = 0
    clean_data = []
    try:
        with open(DB_file, "r", newline ="") as f:
            reader = csv.reader(f)
            for r in reader:
                if len(r) == 3:
                    clean_data.append(r)
                else:
                    a += 1
        with open(DB_file, "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerows(clean_data)
        utils.database(f"User cleaned the file and total faulty rows were {a}")
    except FileNotFoundError:
        print("File Not Found!")
    except PermissionError:
        print("Permission Not Given To The User.")
    finally:
        print("Operation Completed.")

def adding_to_database(b):
    with utils.timer():
        try:
            with open(DB_file,"a", newline = "") as csv_writer:
                obj = csv.writer(csv_writer)
                obj.writerow(b)
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                obj =csv.writer(csv_writer)
                obj.writerow(b)
        else:
            print("Added to the File.")
        finally:
            print("Operation Complete.")