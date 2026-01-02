from slot import slot_bet_result
from black_jack import black_jack
from roulette import roulette
from random import randint


def main():

    player_credits = 10000
    casino_menu(player_credits)

    

def banner():
    print("\n" + "="*46)
    print("                PYARCADE CASINO  ")
    print("="*46)

def divider():
    print("-"*46)

def casino_menu(player_credits):

    

    while True:

        banner()
        print("\nChoose a game:\n")
        print("1️⃣  Slot Machine")
        print("2️⃣  Black Jack")
        print("3️⃣  Roulette")
        print("0️⃣  Exit")

        divider()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            player_credits = slot_bet_result(player_credits)
        elif choice == "2":
            player_credits = black_jack(player_credits)
        elif choice == "3":
            player_credits = roulette(player_credits)
        elif choice == "0":
            print("\nThanks for playing PyArcade Casino \n")
            break
        else:
            print("\n Invalid choice. Try again.")

        play = input(("\nContinue Playing? Yes/No ")).strip().lower()
        if play == 'yes':
            continue
        elif play == 'no':
            break

if __name__ == '__main__':
    main()