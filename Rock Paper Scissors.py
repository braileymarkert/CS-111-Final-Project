import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors")
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score <3:
        player_choice = input("Choose rock, paper, or scissors: ")
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "Tie":
            print("It's a tie!")
        elif result == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer winds this round!")
            computer_score += 1

def main():
    while True:
        play_game()
        again = input("Would you like to play again?: ")
        if again == "no":
            print("Thank you for playing")
            break
        elif again == "yes":
            continue

main()
