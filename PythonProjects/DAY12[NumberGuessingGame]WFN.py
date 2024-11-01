import random

string_list = ["Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100."
               "\nChoose a difficulty. Type 'easy' or 'hard':", "No guesses remain. You lose.",
               "Play again? Type 'play' or 'exit':", "You have ",
               " attempts remaining to guess the number.\nMake a guess:", "Invalid input. Returning to menu.",
               "You win!","Too low.","Too high."]

win = 0
secret = 0
def secret_num():
    global secret
    secret = random.choice(range(1,101))

def attempts_set():
    global attempts
    if user_diff.lower() == "hard":
        attempts = 5
    elif user_diff.lower() == "easy":
        attempts = 10
def guess_check():
    global win
    global attempts
    global secret
    if user_guess == secret:
        win = 1
        print(string_list[6])
    elif user_guess < secret:
        attempts -= 1
        print(string_list[7])
    elif user_guess > secret:
        attempts -= 1
        print(string_list[8])

def game_check():
    global attempts
    global game
    if attempts == 0:
        game = 0

while True:
    game = 1
    attempts = 10
    user_diff = input(string_list[0])
    if user_diff.lower() == "easy" or user_diff.lower() == "hard":
        attempts_set()
        secret_num()
        while True:
            if win == 0:
                user_guess = int(input(f"{string_list[3]}{attempts}{string_list[4]}"))
                guess_check()
                game_check()
                if game == 0:
                    print(string_list[1])
                    break
            elif win == 1:
                break
        user_choice = input(string_list[2])
        if user_choice.lower() == "exit":
            break
    else:
        print(string_list[5])




