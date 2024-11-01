import random

# Keep track of games played and won by the user
games_played = 0
games_won = 0

# Define the possible choices
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    global games_won

    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        games_won += 1
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    global games_played
    games_played += 1

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

def display_score():
    print(f"Games played: {games_played}")
    print(f"Games won by you: {games_won}")

# Main game loop
def main():
    while True:
        play_game()
        display_score()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
