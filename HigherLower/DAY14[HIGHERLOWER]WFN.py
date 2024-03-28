import random
from smdata import smdata
string_list = ["Welcome to Higher Lower!", "Invalid entry. Check your spelling!",
               "Type 'play' to play again, or 'exit' to close program", "Sorry, that's wrong. Final Score: "]

def celeb_gen():
    result = random.choice(smdata)
    return result

def dupe_check():
    if celeb1 == celeb2:
        return True
    else:
        return False

def guess_check():
    global current_score
    global game
    if user_guess.lower() == celeb1['name'].lower() and celeb1['follower_count'] > celeb2['follower_count']:
        current_score += 1
        print(f"You're Right! Current Score:{current_score}")
    elif user_guess.lower() == celeb1['name'].lower() and celeb1['follower_count'] < celeb2['follower_count']:
        game = 0
    elif user_guess.lower() == celeb2['name'].lower() and celeb2['follower_count'] > celeb1['follower_count']:
        current_score += 1
        print(f"You're Right! Current Score:{current_score}")
    elif user_guess.lower() == celeb2['name'].lower() and celeb2['follower_count'] < celeb1['follower_count']:
        game = 0

def guess_check2():
    if user_guess.lower() != celeb1['name'].lower() and user_guess.lower() != celeb2['name'].lower():
        return True

def game_check():
    if game == 0:
        print(f"{string_list[3]}{current_score}")
        return True

def score_reset():
    global current_score
    current_score = 0

print(string_list[0])
current_score = 0

while True:
    game = 1
    celeb1, celeb2 = celeb_gen(), celeb_gen()
    if not dupe_check():
        user_guess = input(f"Who has more followers? (in millions)\n{celeb1['name']}, "
                           f"a {celeb1['description']}, from {celeb1['country']}...\n"
                           f"or {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}?")
        if guess_check2():
            print(string_list[1])
        elif not guess_check2():
            guess_check()
            if game_check():
                score_reset()
                user_choice = input(string_list[2])
                if user_choice.lower() == "exit":
                    break




