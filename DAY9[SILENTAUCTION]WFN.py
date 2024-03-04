string_list = ["Welcome to the silent auction program!","What is your name?","What is your bid?",
               "Are there any other bidders? Type 'yes' or 'no'","Invalid input. Returning to menu..."]

my_dict = {}

print(string_list[0])
bidder_name = input(string_list[1])
bidder_bid = int(input(string_list[2]))
my_dict[bidder_name] = bidder_bid

while True:
    bid_question = input(string_list[3])
    if bid_question.lower() == "yes":
        bidder_name = input(string_list[1])
        bidder_bid = int(input(string_list[2]))
        my_dict[bidder_name] = bidder_bid
    elif bid_question.lower() == "no":
        max_key = max(my_dict, key=my_dict.get)
        max_value = my_dict[max_key]
        print(f"The winner is {max_key.capitalize()} with a bid of ${max_value}!")
        break
    else:
        print(string_list[4])

