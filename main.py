import myutils
while True:
    user_name = myutils.name()
    user_yes_no = myutils.yes_no()
    if user_yes_no == "Yes":
        print(user_name)
        break
    else:
        print("You can try diff. name.")
filename = input("Enter the file name: ")
myutils.check_file(filename)