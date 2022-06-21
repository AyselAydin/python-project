import random

#1 -> Rock 2 -> Paper 3 -> Scissors
loses_to = {
    1: 3, #Rock vs Scissor -> Rock wins
    2: 1, #Rock vs Paper -> Paper wins
    3: 2  #Paper vs Scissor -> Scissor wins
}

def print_result(winner = "Computer"):
    global computer_score, player_score
    print(f'Computer choice: {computer_choice}\nWinner: {winner}')

    if winner == "Computer":
        computer_score += 100
    else:
        player_score += 100

player_score, computer_score = 0, 0
computer_choice = 1

print("\nWelcome to Rock Paper Scissors Game!\n" + ("-" * 36))

print("Winning rules of the Rock-Paper-Scissor game: \n"
                                +"Rock vs Paper -> paper wins \n"
                                + "Rock vs Scissor -> Rock wins \n"
                                +"Paper vs Scissor -> Scissor wins")
while True:
    print("\n 1 -> Rock\n 2 -> Paper\n 3 -> Scissors\n If you want to exit the game, press any key.\n")
    player_choice = int(input("Enter your choice: "))
    computer_choice = random.choice([1, 2, 3])
    
    if player_choice == computer_choice:
        print("Player and computer made the same choice, play again")
    elif player_choice not in [1, 2, 3]:
        break
    elif player_choice == loses_to[computer_choice]:
        print_result()
    elif computer_choice == loses_to[player_choice]:
        print_result("Player")

print(f'\nPlayer Score: {player_score}\nComputer Score: {computer_score}')

if player_score < computer_score:
    print(f'Player loses to computer by {computer_score - player_score} points')
elif player_score > computer_score:
    print(f'Computer loses to player by {player_score - computer_score} points')
else:
    print("Player and computer won the same score")