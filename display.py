from grade_manager import utils
import pandas as pd
from grade_manager import DB_file
from grade_manager import database

def option_2():
    with utils.timer():
        try:
            db = pd.read_csv(DB_file)
            db['marks'] = pd.to_numeric(db['marks'],errors = "coerce")
            print(db.groupby('subject')['marks'].mean())
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        except PermissionError:
            print("File could be locked or file is already opened in another tab or file is on read-only mode. ")
        finally:
            print("Operation Complete.")

def option_3():
    with utils.timer():
        try:
            db = pd.read_csv(DB_file)
            db['marks'] = pd.to_numeric(db['marks'],errors = "coerce")
            clean_db = db.dropna(subset=['marks'])
            print(clean_db.loc[clean_db['marks'].idxmax()])
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        except PermissionError:
            print("File could be locked or file is already opened in another tab or file is on read-only mode. ")
        finally:
            print("Operation Complete.")

def option_4():
    with utils.timer():
        try:
            db = pd.read_csv(DB_file)
            db["marks"] = pd.to_numeric(db["marks"],errors = "coerce")
            clean_db = db.dropna(subset=['marks'])
            print(clean_db.loc[clean_db['marks'].idxmin()])
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        except PermissionError:
            print("File could be locked or file is already opened in another tab or file is on read-only mode. ")
        finally:
            print("Operation Complete.")

def option_5():
    with utils.timer():
        try:
            db = pd.read_csv(DB_file)
            if not db.empty:
                print(db.head())
            else:
                print("There is no data present!")
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        except PermissionError:
            print("File could be locked or file is already opened in another tab or file is on read-only mode. ")
        finally:
            print("Operation Complete.")

def option_6():
    with utils.timer():
        try:
            db = pd.read_csv(DB_file)
            if not db.empty:
                print(db)
            else:
                print("There is no data present!")
        except FileNotFoundError:
            print("File Not Found! Creating New File...")
            with open(DB_file,"a",newline="") as csv_writer:
                pass
        except pd.errors.ParserError:
            print("File is corrupted! Fix it or delete it.")
        except PermissionError:
            print("File could be locked or file is already opened in another tab or file is on read-only mode. ")
        finally:
            print("Operation Complete.")

def option_8():
    with utils.timer():
        database.repair_file()