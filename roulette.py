import random
from slot import bet_input
from slot import slow_print
from slot import play_again
def main():
    player_credits = 10000
    player_credits = roulette(player_credits)



def roulette_bet():

    #allowed values
    allowed_bets = ['straight', 'color', 'even/odd', 'high/low', 'dozen']
    allowed_values = ['black', 'red']
    bets = {}  # this list ius what it returns
    print(f'Allowed Bets: straight, color, even/odd, high/low')

    while True:
        typ = input('Choose the type of bet: ').strip().lower()
        if typ in allowed_bets:
            bets['type'] = typ
            break
        else:
            print("Invalid bet type. Try again.")

    if typ == 'straight':
        while True:
            try :
                value = int(input('Choose the value of bet(1-36): ').strip().lower())
                if value in range(1,37):
                    # bets.append(value)
                    bets['value'] = value
                    break
                else:
                        raise(ValueError)
                            #     print("Invalid bet value. Try again with numbers from 0 to 36.")
            except ValueError:

                     print("Invalid bet value. Try again with numbers from 0 to 36.")

    if typ == 'color':
        while True:
            try :
                value = (input('Choose the value of bet(red or black): ').strip().lower())
                if value in allowed_values:
                    bets['value'] = value
                    # bets.append(value)
                    break
                else:
                    raise(ValueError)
                            #     print("Invalid bet value. Try again with numbers from 0 to 36.")
            except ValueError:
                    print("Invalid bet value. Try again with values - Black & Red")

                    # print("Invalid bet value. Try again with numbers from 0 to 36.")


    if typ == 'even/odd':
        while True:
            try :
                value = (input('Choose the value of bet(even or odd): ').strip().lower())
                if value in ['even', 'odd']:
                    # bets.append(value)
                    bets['value'] = value
                    break

                else:
                    raise(ValueError)
                            #     print("Invalid bet value. Try again with numbers from 0 to 36.")
            except ValueError:

                    print("Invalid bet value. Try again with values - even or odd")


    if typ == 'high/low':
        while True:
            try :
                value = (input('Choose the value of bet(high or low): ').strip().lower())
                if value in ['high', 'low']:
                    # bets.append(value)
                    bets['value'] = value
                    break

                else:
                    raise(ValueError)
                            #     print("Invalid bet value. Try again with numbers from 0 to 36.")

            except ValueError:
                    print("Invalid bet value. Try again with values - high or low")


    while True:
        try:
            amount = int(input('Enter the bet amount: '))
            if amount>0:
                # bets.append(amount)
                bets['amount'] = amount
                break
            else:
                print("Invalid bet amount. Try again.")
        except ValueError:
            print('Enter a valid amount')

    
    return bets
    
def roulette_color(n):

    if n == 0:
        return "Green"
    # european roulette - (0-36)
    if not 1 <= n <= 36:
        return "Invalid"

    if (1 <= n <= 10) or (19 <= n <= 28):
        return "red" if n % 2 else "black"
    else:
        return "black" if n % 2 else "red"

def roulette_number():
    
    return random.randint(0,36)

def banner():
    print("\n" + "="*42)
    print("             ROULETTE CASINO  ")
    print("="*42)
    print()
def divider():
    print("="*42)


def roulette(player_credits):

    while True:
        #printing the game banner
        banner()
        print(f"Credits: {player_credits}\n")   

        # bet_type, value, amount = roulette_bet()
        bet =  roulette_bet()

        if bet['amount'] > player_credits:
            print("Not enough credits!")
            return player_credits

        player_credits -= bet['amount']

        bet_type = bet['type']
        value = bet['value']
        amount = bet['amount']

        number = roulette_number()
        color = roulette_color(number)

        slow_print("Spinning the wheel...")
        slow_print(f'Ball landed on : {number} {color.upper()}')

        winnings = 0

        print("\n============== RESULT ==============")

        if bet_type == 'straight' :
            if value == number:
                winnings+=amount*35
                print(f"\nJackpot! You won {amount* 35}!")
            else:
                print('You Loose. Better luck next time ')

        if bet_type == 'color':
            if value == color:
                winnings+= amount*2
                print(f"\nJackpot! You won {amount*2 }!")
            else:
                print('You Loose. Better luck next time ')

        if bet_type == 'even/odd':
            if value == 'even' and number!=0 and number % 2==0:
                winnings+= amount*2
                print(f"\nJackpot! You won {amount*2 }!")

            elif value == 'odd' and number % 2 !=0:
                winnings+= amount*2
                print(f"\nJackpot! You won {amount*2 }!")

            else:
                print('You Loose. Better luck next time ')

        if bet_type == 'high/low':
            if value == 'high' and 19<=number<=36:
                winnings+= amount*2
                print(f"\nJackpot! You won {amount*2 }!")

            elif value == 'low' and 1<=number<=18 :
                winnings+= amount*2
                print(f"\nJackpot! You won {amount*2 }!")
            else:
                print('You Loose. Better luck next time ')

        divider()

        if winnings:
            player_credits += winnings
            print(f"\n Updated Credits: {player_credits}")   
 
        
        if not play_again():
            break

        
    return player_credits


if __name__ == '__main__':
    main()
