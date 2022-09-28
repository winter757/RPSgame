import random

total_turns = []
win_history = []
computer_turns = []
human_turns = []

def play_again():

    turns = ["Rock", "Paper", "Scissors"]

    human_turn = input("Input human turn: ")
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    print(f"Human: {human_turn} vs. Computer: {computer_turn}")

    if human_turn == "Rock" and computer_turn == "Scissors":
        print("Human wins!")
        win_history.append("Win")
    elif human_turn == "Paper" and computer_turn == "Rock":
        print("Human wins!")
        win_history.append("Win")
    elif human_turn == "Scissors" and computer_turn == "Paper":
        print("Human wins!")
        win_history.append("Win")
    elif human_turn == computer_turn:
        print("Draw.")
        win_history.append("Draw")
    else:
        print("Computer wins!")
        win_history.append("Lose")

while True:
    restart = input("Do you want to play again? Y/N: ")
    if restart == "Y":
        play_again()
        total_turns.append(restart)
    elif restart == "N":
        break
    else:
        print("Enter a valid answer.")

print(f"You have played {len(total_turns)} times.")
print(f"Your game history: {win_history}")
print(f"The moves made by you were: {human_turns}")
print(f"The moves made by the computer were: {computer_turns}")
