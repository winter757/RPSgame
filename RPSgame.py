human_turn = input("Input human turn: ")
computer_turn = input("Input computer turn: ")

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
