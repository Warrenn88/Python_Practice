import random

string_list = ["Welcome to Blackjack!\nDealer hits on all 16's. Ace is 1 or 11. 21 can tie."]

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
         9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

def get_hand_value(hand):
    total = 0
    num_aces = 0
    for card_value in hand:
        total += card_value
        if card_value == 11:
            num_aces += 1
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total

def card_generator():
    card = random.choice(cards)
    return card

print(string_list[0])

while True:
    user_hand = [card_generator(), card_generator()]
    comp_hand = [card_generator(), card_generator()]
    uvalue, cvalue = get_hand_value(user_hand), get_hand_value(comp_hand)
    user_choice = input(f"Your hand is {user_hand} and the dealer\n is showing {comp_hand[0]}. Hit or stay?")
    while True:
        if user_choice.lower() == "stay":
            if cvalue > 16 and cvalue > uvalue:
                print(f"Dealer hand was {comp_hand} with a value of {cvalue}. DEALER WINS!")
                break
            elif cvalue <= 16:
                while get_hand_value(comp_hand) <= 16:
                    comp_hand.append(card_generator())
                    cvalue = get_hand_value(comp_hand)
                if cvalue > 21:
                    print(f"Dealer hand was {comp_hand} with a value of {cvalue} Dealer BUSTS - YOU WIN!")
                    break
                elif cvalue > uvalue:
                    print(f"Dealer hand was {comp_hand} with a value of {cvalue} Dealer WINS!")
                    break
                elif uvalue > cvalue:
                    print(f"Dealer hand was {comp_hand} with a value of {cvalue} YOU WIN!")
                    break
                elif uvalue == cvalue:
                    print(f"Dealer hand was {comp_hand} with a value of {cvalue} PUSH - YOU TIE")
                    break
        elif user_choice.lower() == "hit":
                user_hand.append(card_generator())
                uvalue = get_hand_value(user_hand)
        else:
            print("Invalid input. Returning to menu")
            break





