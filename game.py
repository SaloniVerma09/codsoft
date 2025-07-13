import random  

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"  

def play_game():
    user_score = 0         
    computer_score = 0    
    round_num = 1         

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        print(f"\nRound {round_num}")  

        user_choice = get_user_choice()        
        computer_choice = get_computer_choice() 

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)  # Decide who won

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score :- You: {user_score} | Computer: {computer_score}")

        # Ask if the player wants to continue
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break  
        round_num += 1  
    print("\nThanks for playing!")
    print(f"Final Score :- You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    play_game()  
