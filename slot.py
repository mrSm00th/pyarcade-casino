import random
def main():

    player_credits = 10000
    player_credits = slot_bet_result(player_credits)


def play_again():
    while True:
        choice = input("\nPlay this game again? (yes/no): ").strip().lower()
        if choice in ("yes", "no"):
            return choice == "yes"
        print("Please type yes or no.")

def slot_bet_result(player_credits):
    while True:
        print("\n========= SLOT MACHINE =========\n")
        print(f"Credits: {player_credits}")

        bet = bet_input(player_credits)
        player_credits -= bet

        payout = slot_machine(bet)
        player_credits += payout

        print(f"\n Updated Credits: {player_credits}")

        if not play_again():
            break
    return player_credits


def bet_input(player_credits):

    while True:
        try:
            bet = int(input("Enter your bet : "))
            if bet <= 0 :
                print("Bet must be positive.")
                
            elif bet > player_credits:
                print(" Not enough credits.")

            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a numeric value for the bet amount.")

def slow_print(text):
    import time
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.02)
    print()

def slot_machine(bet):

    symbols = ['A', 'B', 'C', 'D', 'E', '⭐', '💎']
    weights = [30, 25, 20, 15, 10, 4, 1]
    # weights = [150, 120, 100, 75, 45, 5, 1]
    reel = random.choices(symbols, weights=weights, k=3) 
    
    
    slow_print("Spinning...\n")
    slow_print(" | ".join(reel))

    payout = slot_payout(reel, bet)
    return payout



def slot_payout(reel, bet):

    print("\n============= RESULT =============")


    if reel[0] == reel[1] == reel[2] == '💎':
        payout = bet * 10
        print(f"\nJackpot! You won {payout}!")
    elif reel[0] == reel[1] == reel[2] == '⭐':
        payout = bet * 5
        print(f"\nGreat! You won {payout}!")
    elif reel[0] == reel[1] == reel[2]:
        payout = bet * 2
        print(f"\nYou won {payout}!")
    else:
        payout = 0
        print("\nBetter luck next time!")

    return payout

if __name__ =='__main__':
    main()