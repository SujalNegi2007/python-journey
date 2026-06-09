from pathlib import Path
import csv
db_path = Path("database.csv")

#========first stage of reading========#
def reading(file_path: Path):
    with file_path.open("r", encoding = "utf-8") as file:
        c = 0
        for line in file:
            c +=1
            yield (c, line.strip())

def finder(a):
    for c,line in a:
        if "error" in line.lower():
            yield (c,line)

def line_of_error(b):
    for c,line in b:
        yield f"[Error Found In Line]: {c} | Crash -> {line.upper()}"


gen_reading = reading(db_path)
gen_finder = finder(gen_reading)
gen_line_of_error = line_of_error(gen_finder)

print("Starting the pipeline".center(100,"="))
for line in gen_line_of_error:
    print(line)
print("Operation Completed".center(100,"="))
