import random

choice = input("Heads or Tails?")
result = random.randint(0,1)
if result == 0:
    result = "heads"
else:
    result = "tails"

if result == choice.lower():
    print(f"You win! It's {result}!")
if result != choice.lower():
    print(f"You lose! It's {result}!")



