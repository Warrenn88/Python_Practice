string_list = ["Type 'max' to calculate max,\nor 'chart' to calculate lifting chart:",
               "Enter weight lifted in Lbs:","Enter number of complete reps performed:",
               f"Your max weight for this lift is around","Menu or exit?", "Returning to menu ...",
               "Exiting program ...","Invalid input, returning to menu...",
               "To calculate your lifting chart,\nplease enter your maximum lift to the nearest pound:",
               "Welcome to Warren's Weight Lifting Program",]
while True:
    print(string_list[9])
    request1 = input(string_list[0])
    if request1.lower() == "max":
        weight, reps = float(input(string_list[1])), int(input(string_list[2]))
        result = round(weight/(1.0278 - (.0278 * reps)))
        print(string_list[3], str(result) + " lbs.")
        request2 = input(string_list[4])
        if request2.lower() == "menu":
            print(string_list[5])
        elif request2.lower() == "exit":
            print(string_list[6])
            break
        else:
            print(string_list[7])
    elif request1.lower() == "chart":
        max = float(input(string_list[8]))
        def percent_calculator(max):
            result = (f"100% = {round(max)} lbs\n90% = {round(max*.9)} lbs\n80% = {round(max*.8)} lbs"
                      f"\n70% = {round(max*.7)} lbs\n60% = {round(max*.6)} lbs\n50% = {round(max*.5)} lbs")
            return result
        print(percent_calculator(max))
        request3 = input(string_list[4])
        if request3.lower() == "menu":
            print(string_list[5])
        elif request3.lower() == "exit":
            print(string_list[6])
            break
        else:
            print(string_list[7])
    else:
        print(string_list[7])