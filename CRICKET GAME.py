import random

def toss():
    choice = input("Choose Heads or Tails: ").strip().lower()
    toss_result = random.choice(["heads", "tails"])
    print(f"Toss result: {toss_result}")
    if choice == toss_result:
        print("You won the toss!")
        decision = input("Do you want to bat or bowl first? (bat/bowl): ").strip().lower()
        return "user", decision
    else:
        print("Computer won the toss!")
        decision = random.choice(["bat", "bowl"])
        print(f"Computer chose to {decision} first.")
        return "computer", decision

def play_innings(player, target=None):
    runs = 0
    while True:
        user_input = int(input(f"{player.capitalize()}'s turn (show a number between 1 and 6): "))
        computer_input = random.randint(1, 6)
        print(f"Computer shows: {computer_input}")
        if user_input == computer_input:
            print(f"{player.capitalize()} is out!")
            break
        else:
            runs += user_input if player == "user" else computer_input
        print(f"{player.capitalize()}'s score: {runs}")
        if target and runs > target:
            print(f"{player.capitalize()} wins the match!")
            return runs
    return runs

def hand_cricket_game():
    print("Welcome to Hand Cricket!")
    toss_winner, toss_decision = toss()

    if toss_winner == "user":
        if toss_decision == "bat":
            user_runs = play_innings("user")
            print(f"Your score: {user_runs}")
            print("Computer's turn to chase!")
            computer_runs = play_innings("computer", user_runs)
        else:
            computer_runs = play_innings("computer")
            print(f"Computer's score: {computer_runs}")
            print("Your turn to chase!")
            user_runs = play_innings("user", computer_runs)
    else:
        if toss_decision == "bat":
            computer_runs = play_innings("computer")
            print(f"Computer's score: {computer_runs}")
            print("Your turn to chase!")
            user_runs = play_innings("user", computer_runs)
        else:
            user_runs = play_innings("user")
            print(f"Your score: {user_runs}")
            print("Computer's turn to chase!")
            computer_runs = play_innings("computer", user_runs)

    print(f"Final Scores: You - {user_runs}, Computer - {computer_runs}")
    if user_runs > computer_runs:
        print("You win!")
    elif user_runs < computer_runs:
        print("Computer wins!")
    else:
        print("It's a tie!")

hand_cricket_game()
