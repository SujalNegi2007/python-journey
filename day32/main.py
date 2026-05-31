#Main Menu
import utils
while True:
    user_name = input("\nWelcome To The Question Game!\nPlease Enter Your Name: ").capitalize().strip()
    first_name = utils.name(user_name)
    question = utils.load_questions()
    d = int(input("\nEnter How Many Questions You Want To Answer: "))
    if 0 < d <= len(question):
        total_answered = 0
        answered_right = 0
        for i in range(d):
            print(f"{question[i]["question"]}\n{question[i]["options"]}")
            while True:
                num = input("\nEnter Your Answer: ").upper().strip()
                if num == question[i]["answer"]:
                    print("You Are Correct!\n")
                    answered_right +=1
                    total_answered +=1
                    break
                elif num in ["A","B","C","D"]:
                    print("You Are Wrong!\nAnswer Was {question[i]["answer"]}\n")
                    total_answered +=1
                    break
                else:
                    print("Wrong Input!\n")
        print(f"You Have Answered {answered_right} out of {total_answered}.")
    elif d <= 0:
        print("Please select intergers that are more than 0.")
    else:
        print("We Don't Have That many questions to ask")
