import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm','n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']

symbols = ['!','@', '#', '$','%', '^', '&',
           '*', '(', ')', '-', '=', '+', '>',
           '<', '[', ']','~']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Welcome to Warren's Password Generator!")
letters_user = input("How many letters would you like in your password? (Max:52)")
symbols_user = input("How many symbols would you like? (Max:18)")
numbers_user = input("How many numbers would you like? (Max:10)")
final_letters = random.sample(letters, k=int(letters_user))
final_symbols = random.sample(symbols, k=int(symbols_user))
final_numbers = random.sample(numbers, k=int(numbers_user))

final_list = final_letters + final_symbols + final_numbers
random.shuffle(final_list)
x ="".join(final_list)
print(x)


