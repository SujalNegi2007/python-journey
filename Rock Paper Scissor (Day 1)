import random
print("Welcome to rock, paper and scissor!\n")
def get_choices():
    player_chose = input("Enter Your Move(rock, paper, scissor): ")
    options = [ "rock" , "paper" , "scissor" ]
    computer_chose = random.choice(options)
    choices = { "player": player_chose, "opponent" : computer_chose }
    return choices

def check_win(player, computer):
    print(f"you chose {player} and opponent chose {computer}")
    if player == computer:
        return "It's a draw"
    elif player == "rock":
        if computer == "paper":
            return "paper wrap the rock! You lose!"
        else:
            return "rock smashes scissor! You win!"
    elif player == "paper":
        if computer == "rock":
            return "paper wrap the rock! You win!"
        else:
            return "scissors cut paper! You lose!"
    else:
        if computer == "paper":
            return "scissors cut paper! You win!"
        else:
            return "rock smashes scissor! You lose!"
abc = get_choices()
result = check_win(abc["player"], abc["opponent"])
print(result)
