import random

string_list = ["Welcome to Blackjack!\nDealer hits on 16.\nAce is 1 or 11.\n21 can tie."]
cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
         9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11 ,11 ,11]

def card_generator():
    random_cards= (random.choice(cards), random.choice(cards))
    return random_cards

player_hand, dealer_hand = card_generator(), card_generator()
player_hand_value, dealer_hand_value = sum(player_hand), sum(dealer_hand)
print(string_list[0])
print(f"Your hand is {player_hand} and the dealers\n first card is a {dealer_hand[0]}")
user_response = input("Will you hit or will you stay?")
if user_response.lower() == "stay":
    print(f"Dealer has a hand of {dealer_hand}")
    if player_hand_value < 16 and dealer_hand_value > 16:
        print(f"Dealer wins, their hand of {dealer_hand} beats players hand of {player_hand}")
    elif dealer_hand_value > 16 and player_hand_value > dealer_hand_value:
        print(f"Player wins, their hand of {player_hand} beats dealers hand of {dealer_hand}")
    elif dealer_hand_value < 17:
        while dealer_hand_value < 17:
            print(f"Dealer keeps hitting under 17 ... ")
            dealer_draw = random.choice(cards)
            dealer_hand_value += dealer_draw
            print(f"Dealer draws a {dealer_draw} for a total of {dealer_hand_value}")
        if dealer_hand_value > 21:
            print(f"Dealer BUSTS, you WIN! Dealer's final hand value was {dealer_hand_value}!")
        elif dealer_hand_value <= 21 and dealer_hand_value > player_hand_value:
            print(f"Dealer wins, their total of {dealer_hand_value} beats player who has {player_hand_value}")
        elif dealer_hand_value <= 21 and dealer_hand_value < player_hand_value:
            print(f"Player wins, their total of {player_hand_value} beats dealer who has {dealer_hand_value}")
        elif dealer_hand_value <= 21 and dealer_hand_value == player_hand_value:
            print(f"Hand is a Push. Dealer has a total of {dealer_hand_value} and player has a total of {player_hand_value}")
        else:
            print(f"this is a debugging report. {dealer_hand_value},{player_hand_value}")





