step1 = input("Welcome to Treasure Island!\nYour mission is to find the treasure.\nWould you like to go left or right?")
if step1.lower() == "left":
    step2 = input("You come to a river. Will you swim or wait?")
    if step2.lower() == "wait":
        step3 = input("You wait for a boat and cross the river.\nWhich will you choose?\nRed, Blue, or Yellow?")
        if step3.lower() == "red":
            print("You were burned by fire. GAME OVER")
        elif step3.lower() == "yellow":
            print("You WIN!")
        elif step3.lower() == "blue":
            print("You were eaten by beasts. GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("You were attacked by trout. GAME OVER.")
else:
    print("You fall into a hole. GAME OVER")
