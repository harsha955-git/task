import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        player = input("Enter rock, paper, or scissors (or quit): ").lower()
        if player == "quit":
            break
        if player not in ["rock", "paper", "scissors"]:
            print("Invalid input.")
            continue
        computer = get_computer_choice()
        print("Computer chose:", computer)
        print(decide_winner(player, computer))

play_game()

