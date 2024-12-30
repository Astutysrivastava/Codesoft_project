import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_results(user_choice, computer_choice, result):
    """Display the choices and the result of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose your move: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        display_results(user_choice, computer_choice, result)
        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank you for playing Rock-Paper-Scissors!")
            print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    main()
