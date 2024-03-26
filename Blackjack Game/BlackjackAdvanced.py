import random

string_list = ["Welcome to Blackjack!\nDealer hits on all 16's. Ace is 1 or 11. 21 can tie.",
               "Invalid input, returning to menu", "Type 'deal' for a new hand, or 'exit' to quit:",
               "Invalid bet", "You don't have enough for the minimum bet. Game over.",
               "You don't have enough $ to double down!", "You don't have enough $ to split!",
               " Place your bet. Min bet $10. You have $"]

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
         9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

player_bank = 100
user_bet = 0
win = 0
game = 1
ddcheck = 0

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
    global win
    if get_hand_value(user_hand) > 21:
        win = 0
        print(f"Player has {user_hand} with a value of {get_hand_value(user_hand)}. PLAYER BUSTS. YOU LOSE")
    elif get_hand_value(comp_hand) > 21:
        win = 1
        print(f"Dealer has {comp_hand} with a value of {get_hand_value(comp_hand)}. DEALER BUSTS. YOU WIN")
    elif get_hand_value(user_hand) == get_hand_value(comp_hand):
        win = 2
        print(f"Dealer has {comp_hand} with a value of {get_hand_value(comp_hand)}. PUSH")
    elif get_hand_value(user_hand) < get_hand_value(comp_hand):
        win = 0
        print(f"Dealer has {comp_hand} with a value of {get_hand_value(comp_hand)}. YOU LOSE")
    elif get_hand_value(user_hand) > get_hand_value(comp_hand):
        win = 1
        print(f"Dealer has {comp_hand} with a value of {get_hand_value(comp_hand)}. YOU WIN")

def user_hitter():
    variable = "hit"
    while variable.lower() == "hit":
        user_hand.append(card_generator())
        if get_hand_value(user_hand) > 21:
            break
        else:
            variable = input(f"Your hand is {user_hand} and the value is {get_hand_value(user_hand)}. Hit or stay?")

def split1_solver():
    user_choice2 = input(f"Your two new hands are {hand1} and {hand2}."
                         f"\nFor hand 1, hit or stay?")
    if user_choice2.lower() == "hit":
        user_hitter()
        winning_hand()
    elif user_choice2.lower() == "stay":
        winning_hand()
    else:
        print(string_list[1])
        split1_solver()

def split2_solver():
    user_choice2 = input(f"Your second new hand is {hand2}. Hit or stay?")
    if user_choice2.lower() == "hit":
        user_hitter()
        winning_hand()
    elif user_choice2.lower() == "stay":
        winning_hand()
    else:
        print(string_list[1])
        split2_solver()

def double_down():
    global user_bet
    global player_bank
    user_bet = user_bet * 2
    user_hand.append(card_generator())
    print(f"Player doubles down and has a hand of"
          f" {user_hand} with a value of {get_hand_value(user_hand)}")

def double_down_check():
    global ddcheck
    global user_bet
    global player_bank
    if user_bet * 2 <= player_bank:
        ddcheck = 1
    else:
        ddcheck = 0

def player_bet():
    global user_bet
    while True:
        user_bet = int(input(f"{string_list[7]}{player_bank}:"))
        if user_bet >= 10 and user_bet <= player_bank:
            break
        else:
            print(string_list[3])

def bank_calc():
    global player_bank
    global user_bet
    global win
    if win == 2:
        print(f"Money returned. Your balance is ${player_bank}")
    elif win == 1:
        player_bank += user_bet
        print(f"You won ${user_bet}! Your balance is ${player_bank}")
    elif win == 0:
        player_bank -= user_bet
        print(f"You lost ${user_bet}. Your balance is ${player_bank}")
    game_check()

def game_check():
    global player_bank
    global game
    if player_bank <= 9:
        game = 0
        print(string_list[4])

print(string_list[0])
while game == 1:
    user_hand = [card_generator(), card_generator()]
    comp_hand = [card_generator(), card_generator()]
    card_auto_hitter()
    user_choice1 = input(string_list[2])
    if user_choice1.lower() == "deal":
        player_bet()
        while True:
            if user_hand[0] == user_hand[1]:
                user_choice = input(f"Your hand is {user_hand} and the dealer is showing {comp_hand[0]}.\n"
                                    f"Hit, stay, split, or double down?")
                if user_choice.lower() == "stay":
                    winning_hand()
                    bank_calc()
                    break
                elif user_choice.lower() == "hit":
                    user_hitter()
                    winning_hand()
                    bank_calc()
                    break
                elif user_choice.lower() == "split":
                    double_down_check()
                    if ddcheck ==1:
                        hand1 = [user_hand[0], card_generator()]
                        hand2 = [user_hand[1], card_generator()]
                        user_hand = hand1
                        split1_solver()
                        bank_calc()
                        user_hand = hand2
                        split2_solver()
                        bank_calc()
                    elif ddcheck == 0:
                        print(string_list[6])
                elif user_choice.lower() == "double down":
                    double_down_check()
                    if ddcheck == 1:
                        double_down()
                        winning_hand()
                        bank_calc()
                        break
                    elif ddcheck == 0:
                        print(string_list[5])
                else:
                    print(string_list[1])
            else:
                user_choice = input(f"Your hand is {user_hand} and the dealer is showing {comp_hand[0]}.\nHit, stay, or double down?")
                if user_choice.lower() == "stay":
                    winning_hand()
                    bank_calc()
                    break
                elif user_choice.lower() == "hit":
                    user_hitter()
                    winning_hand()
                    bank_calc()
                    break
                elif user_choice.lower() == "double down":
                    double_down_check()
                    if ddcheck == 1:
                        double_down()
                        winning_hand()
                        bank_calc()
                        break
                    elif ddcheck == 0:
                        print(string_list[5])
                else:
                    print(string_list[1])
    elif user_choice1.lower() == "exit":
        break
    else:
        print(string_list[1])




