print("Welcome to Warren's Weight Lifting Program")

while True:
    request1 = input("Type 'max' to calculate max,\nor 'chart' to calculate lifting table:")
    if request1.lower() == "max":
        weight = int(input("Enter weight lifted in Lbs"))
        reps = int(input("Enter number of complete reps performed"))
        result = weight/(1.0278 - (.0278 * reps))
        resultf = round(result)
        print(f"Based on my calculations, your max weight for \n this lift is around {resultf} lbs")
        request2 = input("Menu or exit?")
        if request2.lower() == "menu":
            print("Returning to menu ...")
        elif request2.lower() == "exit":
            print("Exiting program ...")
            break
        else:
            print("Invalid input, exiting program...")
            break
    elif request1.lower() == "chart":
        max = int(input("To calculate lifting chart, please enter\nyour maximum lift in pounds."))
        ninety = round(max * .90)
        eighty = round(max * .80)
        seventy = round(max * .70)
        sixty = round(max * .60)
        fifty = round(max * .50)
        print(f"Here are your lifting chart values: \n100% = {max} lbs\n90% = {ninety} lbs\n80% = "
              f"{eighty} lbs\n70% = {seventy} lbs\n60% = {sixty} lbs\n50% = {fifty} lbs")
        request3 = input("Menu or exit?")
        if request3.lower() == "menu":
            print("Returning to menu ...")
        elif request3.lower() == "exit":
            print("Exiting program ...")
            break
        else:
            print("Invalid input, exiting program...")
            break
    else:
        print("Invalid input. Returning to menu.")
