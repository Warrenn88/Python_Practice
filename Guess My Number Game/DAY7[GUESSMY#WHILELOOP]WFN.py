import random
actual_number = random.randint(1, 20)

while True:
    user_number = int(input("Guess my number. It is between 1 and 20"))
    if user_number < 1 or user_number > 20:
        print("That number is outside of the range! try again.")
    elif user_number < actual_number:
        print("Too low! Pick a higher number!")
    elif user_number > actual_number:
        print("Too high! Pick a lower number!")
    elif user_number == actual_number:
        print("YOU WIN!")
        break

