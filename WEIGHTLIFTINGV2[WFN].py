import math

string_list = ["Type 'max' to calculate max,\nor 'chart' to calculate lifting table:",
               "Enter weight lifted in Lbs:","Enter number of complete reps performed:",
               f"Your max weight for this lift is around","Menu or exit?", "Returning to menu ...",
               "Exiting program ...","Invalid input, returning to menu...",
               "To calculate your lifting chart,\nplease enter your maximum lift to the nearest pound:",
               "Welcome to Warren's Weight Lifting Program",]
percent_list = [1,.9,.8,.7,.6,.5]
while True:
    print(string_list[9])
    request1 = input(string_list[0])
    if request1.lower() == "max":
        weight, reps = int(input(string_list[1])), int(input(string_list[2]))
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
        max = int(input(string_list[8]))
        for i in percent_list:
            result = str(round(i * max)),"lbs"
            print(" ".join(result))
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