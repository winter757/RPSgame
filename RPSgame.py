import random

total_turns = []

def play_again():

    turns = ["Rock", "Paper", "Scissors"]

    human_turn = input("Input human turn: ")
    computer_turn = random.choice(turns)

    print(f"Human: {human_turn} vs. Computer: {computer_turn}")

    if human_turn == "Rock" and computer_turn == "Scissors":
        print("Human wins!")
    elif human_turn == "Paper" and computer_turn == "Rock":
        print("Human wins!")
    elif human_turn == "Scissors" and computer_turn == "Paper":
        print("Human wins!")
    elif human_turn == computer_turn:
        print("Draw.")
    else:
        print("Computer wins!")

while True:
    restart = input("Do you want to play again? Y/N: ")
    if restart == "Y":
        play_again()
    elif restart == "N":
        break
    else:
        print("Enter a valid answer.")

    total_turns.append(restart)
    print(f"You have played {len(total_turns)} times.")
