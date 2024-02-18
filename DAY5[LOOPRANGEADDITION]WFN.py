total = 0
user_input = input("Please enter a number between 2 and 1000.\nI would be happy to add all of the\neven numbers together!")
user_mod = int(user_input)+1
for number in range(2,(user_mod),2):
    total += number
    print(total)




