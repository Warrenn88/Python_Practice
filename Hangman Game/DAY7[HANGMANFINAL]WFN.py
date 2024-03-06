import random
word_list = ["valhalla", "tycoon", "metaphor", "nexus"]
hidden_word = random.choice(word_list)
lives = 6
blank_spaces = "_" * len(hidden_word)

while lives > 0:
    print(blank_spaces)
    user_guess = input("Guess a letter: ").lower()
    if user_guess in hidden_word:
        temp = ""
        for i in range(len(hidden_word)):
            if hidden_word[i] == user_guess:
                temp += user_guess
            else:
                temp += blank_spaces[i]
        blank_spaces = temp
        if "_" not in blank_spaces:
            print("You win!!!")
            break
    else:
        lives -= 1
        print(f"Incorrect, you have {lives} left")
if lives == 0:
    print(f"YOU LOSE! The word was {hidden_word}")
