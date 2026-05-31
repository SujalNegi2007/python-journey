import json

def load_questions():
    with open("questions.json", "r") as f:
        question = json.load(f)
    return question

def name(user_name):
    full_name = user_name.split(" ")
    first_name = full_name[0]
    return first_name
