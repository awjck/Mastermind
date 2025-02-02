import player_gameplay
import ai_gameplay

def main():
    '''
    This function allows the player to select the game module they want to run and checks the correctness of
    the entered data. If it's incorrect, it prints a message informing what is wrong.

    '''
    print("Welcome to self-playing version of Mastermind - a game of logic and deduction! Choose your gameplay type:")
    print("1. AI gameplay")
    print("2. Player gameplay")

    try:
        choice = int(input("Your choice: "))

        if choice == 1:
            ai_gameplay.start_ai_gameplay()
        elif choice == 2:
            player_gameplay.start_player_gameplay()
        else:
            print("Incorrect number. Try once more.")

    except ValueError:
        print("You can only pass the number.")

if __name__ == "__main__":
    main()