import random

string_list = ["Welcome to Blackjack!\nDealer hits on all 16's. Ace is 1 or 11. 21 can tie.",
               "Invalid input, returning to menu", "Type 'deal' for a new hand, or 'exit' to quit:"]

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
def card_auto_hitter():
    while get_hand_value(comp_hand) <= 16:
        comp_hand.append(card_generator())

def winning_hand():
    if uvalue > 21:
        print(f"Player has {user_hand} with a value of {uvalue}. PLAYER BUSTS. YOU LOSE")
    elif cvalue > 21:
        print(f"Dealer has {comp_hand} with a value of {cvalue}. DEALER BUSTS. YOU WIN")
    elif uvalue == cvalue:
        print(f"Dealer has {comp_hand} with a value of {cvalue}. PUSH")
    elif uvalue < cvalue:
        print(f"Dealer has {comp_hand} with a value of {cvalue}. YOU LOSE")
    elif uvalue > cvalue:
        print(f"Dealer has {comp_hand} with a value of {cvalue}. YOU WIN")
def user_hitter():
    variable = "hit"
    while variable.lower() == "hit":
        user_hand.append(card_generator())
        uvalue = get_hand_value(user_hand)
        if uvalue >21:
            break
        else:
            variable = input(f"Your hand is {user_hand} and the value is {uvalue}. Hit or stay?")

print(string_list[0])
while True:
    user_hand = [card_generator(), card_generator()]
    comp_hand = [card_generator(), card_generator()]
    card_auto_hitter()
    uvalue, cvalue = get_hand_value(user_hand), get_hand_value(comp_hand)
    user_choice1 = input(string_list[2])
    if user_choice1.lower() == "deal":
        while True:
            user_choice = input(f"Your hand is {user_hand} and the dealer\n is showing {comp_hand[0]}. Hit or stay?")
            if user_choice.lower() == "stay":
                winning_hand()
                break
            elif user_choice.lower() == "hit":
                user_hitter()
                uvalue = get_hand_value(user_hand)
                winning_hand()
                break
            else:
                print(string_list[1])
    elif user_choice1.lower() == "exit":
        break
    else:
        print(string_list[1])







