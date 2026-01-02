import random
from slot import bet_input
from slot import play_again
def main():
    
    player_credits = 1000
    black_jack(player_credits)

def deck_generator():

    suits = ['♠', '♥', '♦', '♣']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = [(value, suit) for suit in suits for value in values]
    return deck

def deal_cards(deck, n):
    return [deck.pop() for _ in range(n)]

def card_print(hand):
    for card in hand:
        print(f'{card[0]}{card[1]}', end =' ')

def hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        value = card[0]

        if value in ['J', 'Q', 'K']:
            total += 10
        elif value == 'A':
            total += 11
            aces += 1
        else:
            total += int(value)

    # Downgrade Aces from 11 → 1 as needed
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total



def black_jack(player_credits):

    while True:
        print("\n================ BLACKJACK ================\n")
        print(f"Credits: {player_credits}\n")    

        bet = bet_input(player_credits)
        
        if bet > player_credits:
            print("Not enough credits!")
            return player_credits

        player_credits -= bet

        winnings = 0
        deck = deck_generator()
        random.shuffle(deck)

        player_hand = deal_cards(deck, 2)
        dealer_hand = deal_cards(deck, 2)

        # Initial display
        player_value = hand_value(player_hand)
        dealer_value = hand_value(dealer_hand)


        print("Your hand:", end=" ")
        card_print(player_hand)
        print(f"\nHand value: {player_value}")

        print(f"Dealer shows: {dealer_hand[0][0]}{dealer_hand[0][1]}")
        print("------------------------------------------")

        # Blackjack checks
        if player_value == 21 and dealer_value == 21:
            winnings += bet
            print("Both hit Blackjack! Push. Bet returned.")
            print("Dealer hand:", end=" ")
            card_print(dealer_hand)
            print(f"\nDealer value: {dealer_value}")
            return player_credits

        if player_value == 21:
            winnings+= int(bet*2.5)
            print(f"Blackjack! You won {int(bet * 2.5)}")
            print("Dealer hand:", end=" ")
            card_print(dealer_hand)
            print(f"\nDealer value: {dealer_value}")
            return player_credits

        if dealer_value == 21:
            print("Dealer hit Blackjack. Better luck next time.")
            print("Dealer hand:", end=" ")
            card_print(dealer_hand)
            print(f"\nDealer value: {dealer_value}")
            return player_credits

        # Player Turn 
        while True:
            print("\nHit → Take another card")
            print("Stand → Keep your hand")

            choice = input("Make choice (Hit/Stand): ").strip().lower()

            if choice == "hit":
                card = deal_cards(deck, 1)
                print("\nYou drew:", end=" ")
                card_print(card)

                player_hand += card
                player_value = hand_value(player_hand)

                print("\nYour hand:", end=" ")
                card_print(player_hand)
                print(f"\nHand value: {player_value}")

                if player_value > 21:
                    print("\nBUST! Better luck next time.")
                    return player_credits

                # player dosen't immediately wins as Dealer can still reach 21 and win
                if player_value == 21:
                    break

            elif choice == "stand":
                break

            else:
                print("Invalid input. Please type Hit or Stand.")

        # Dealer Turn
        print("\nDealer reveals hand:", end=" ")
        card_print(dealer_hand)
        print(f"\nDealer value: {dealer_value}")

        while dealer_value < 17:
            dealer_hand += deal_cards(deck, 1)
            dealer_value = hand_value(dealer_hand)

            print("\nDealer draws:", end=" ")
            print(f"{dealer_hand[-1][0]}{dealer_hand[-1][1]}")
            print("Dealer hand:", end=" ")
            card_print(dealer_hand)
            print(f"\nDealer value: {dealer_value}")

        # Round Results
        print("\n============== RESULT ==============")

        
        if dealer_value > 21:
            winnings+= int(bet*2.5)
            print(f"Dealer busts! You won {bet * 2}")

        
        elif player_value > 21:
            print("You busted. Better luck next time.")

        
        elif dealer_value == 21 and player_value == 21:
            print("Dealer wins with 21. Better luck next time.")

        
        elif dealer_value > player_value:
            print("Dealer wins. Better luck next time.")

        elif dealer_value < player_value:
            winnings+= int(bet*2.5)
            print(f"You win! Payout: {bet * 2}")

        else:
            print("Push! Bet returned.")

        if winnings:
            player_credits+=winnings
            print(f"\nUpdated Credits: {player_credits}")  

        if not play_again():
            break


    return player_credits

if __name__ == '__main__':
    main()