# BlackJack Game

import random

# Define the variables:

Dealer_Cards = []
Player_Cards = []
Num_of_Cards = 0
Card_Needed = []
Num_of_Cards_Pulled = 0
Probability = 0

# Deal the cards

while len(Dealer_Cards) != 2:
    Dealer_Cards.append(random.randint(1, 11))
    if len(Dealer_Cards) == 2:
        print("Dealer has: X &", Dealer_Cards[1])

# Display the cards

while len(Player_Cards) != 2:
    Player_Cards.append(random.randint(1, 11))
    if len(Player_Cards) == 2:
        print("You have: ", Player_Cards)

# Sum of players and dealer's cards

if sum(Dealer_Cards) == 21:
    print("Dealer hit a BLACKJACK & Wins")
elif sum(Dealer_Cards) > 21:
    print("Hurray! Dealer is busted")

# Compare the sum of their cards

while sum(Player_Cards) < 21:

    # Cards still needed for a blackjack
    Num_of_Cards = len(Dealer_Cards) + len(Player_Cards)
    print("There are a total of ", Num_of_Cards, "cards.")
    Card_Needed = 21 - sum(Player_Cards)
    print("You still need", Card_Needed, "to get a BlackJack.")

    # Comparing the needed card against the cards already drawn


    if Card_Needed == Player_Cards[0]:
            Num_of_Cards_Pulled += 1
    elif Card_Needed == Player_Cards[1]:
            Num_of_Cards_Pulled += 1


    if Card_Needed == Dealer_Cards[0]:
            Num_of_Cards_Pulled += 1

    elif Card_Needed == Dealer_Cards[1]:
            Num_of_Cards_Pulled += 1

    print("Number of times favourable card has already been pulled:" , Num_of_Cards_Pulled)


    # probability of getting a blackjack from here if the player hits
    Probability = (4 - Num_of_Cards_Pulled) / (52 - Num_of_Cards)
    print("You have a ", Probability, "% chance of getting a outright BlackJack if you HIT.")


    # Prompting the player for what they want to do
    Player_Response = str(input("Would you like STAY or HIT? "))
    Player_Response = Player_Response.upper()
    if Player_Response == 'HIT':
        Player_Cards.append(random.randint(1, 11))
        print("You now have a total of: " + str(sum(Player_Cards)) + " from these cards", Player_Cards)
    elif Player_Response == 'STAY':
        print("The Dealer has a total of: " + str(sum(Dealer_Cards)) + " with the cards: ", Dealer_Cards)
        print("You now have a total of: " + str(sum(Player_Cards)) + " with the cards: ", Player_Cards)
        if sum(Dealer_Cards) > sum(Player_Cards):
            print("OOPS..DEALER WINS.")
            break
        else:
            print("YOU WIN THIS TIME")
            break
    else:
        print("INVALID INPUT")

if sum(Player_Cards) > 21:
    print("Oh No..YOU BUST")


elif sum(Player_Cards) == 21:
    print("WOWZIEE! You hit the BLACKJACK")
