menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

string_list = ["What would you like? (espresso/latte/cappuccino):\nYou may "
               "also type 'exit' to close the program:", "Please insert coins.",
               "Invalid input. Returning to menu", "Returning"]

def cash_app():
    global cents
    print(string_list[1])
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies"))
    cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies)

def dollar_convert():
    global cents
    global dollars
    dollars = cents/100

def report_check():
    print(f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nMoney: {Money}")

def money_check():
    global dollars
    global Money
    if user_choice.lower() == "espresso" and dollars >= float(menu['espresso']['cost']):
        profit = float(menu['espresso']['cost'])
        change = round(dollars - float(menu['espresso']['cost']), 2)
        Money += profit
        print(f"Success! you purchased an espresso for ${menu['espresso']['cost']}\n"
              f"Your change is ${change}")
    elif user_choice.lower() == "latte" and dollars >= float(menu['latte']['cost']):
        profit = float(menu['latte']['cost'])
        change = round(dollars - float(menu['latte']['cost']), 2)
        Money += profit
        print(f"Success! you purchased a latte for ${menu['latte']['cost']}\n"
              f"Your change is ${change}")
    elif user_choice.lower() == "cappuccino" and dollars >= float(menu['cappuccino']['cost']):
        profit = float(menu['cappuccino']['cost'])
        change = round(dollars - float(menu['cappuccino']['cost']), 2)
        Money += profit
        print(f"Success! you purchased a cappuccino for ${menu['cappuccino']['cost']}\n"
              f"Your change is ${change}")
    else:
        print(f"Not enough $. You were returned ${dollars}")

def espresso_check():
    global Water
    global Coffee
    global Milk
    if Water >= float(menu['espresso']['ingredients']['water']) and Coffee >= float(menu['espresso']['ingredients']['coffee']):
        Water -= float(menu['espresso']['ingredients']['water'])
        Coffee -= float(menu['espresso']['ingredients']['coffee'])
        result = True
        return result
    elif Water < float(menu['espresso']['ingredients']['water']):
        print(f"Not enough water. Espresso requires {(menu['espresso']['ingredients']['water'])}ml\n"
              f"and there is only {Water}ml available. Please refill water.")
    elif Coffee < float(menu['espresso']['ingredients']['water']):
        print(f"Not enough coffee. Espresso requires {(menu['espresso']['ingredients']['coffee'])}g\n"
              f"and there is only {Coffee}g available. Please refill coffee beans.")


def latte_check():
    global Water
    global Coffee
    global Milk
    if Water >= float(menu['latte']['ingredients']['water']) and Coffee >= float(
            menu['latte']['ingredients']['coffee']) and Milk >= float(
            menu['latte']['ingredients']['milk']):
        Water -= float(menu['latte']['ingredients']['water'])
        Coffee -= float(menu['latte']['ingredients']['coffee'])
        Milk -= float(menu['latte']['ingredients']['milk'])
        result = True
        return result
    elif Water < float(menu['latte']['ingredients']['water']):
        print(f"Not enough water. Latte requires {(menu['latte']['ingredients']['water'])}ml\n"
              f"and there is only {Water}ml available. Please refill water.")
    elif Coffee < float(menu['latte']['ingredients']['coffee']):
        print(f"Not enough coffee. Latte requires {(menu['latte']['ingredients']['coffee'])}g\n"
              f"and there is only {Coffee}g available. Please refill coffee beans.")
    elif Milk < float(menu['latte']['ingredients']['milk']):
        print(f"Not enough milk. Latte requires {(menu['latte']['ingredients']['milk'])} ml,\n"
              f"and there is only {Milk}ml available.\nPlease refill milk.")

def cap_check():
    global Water
    global Coffee
    global Milk
    if Water >= float(menu['cappuccino']['ingredients']['water']) and Coffee >= float(
            menu['cappuccino']['ingredients']['coffee']) and Milk >= float(
        menu['cappuccino']['ingredients']['milk']):
        Water -= float(menu['cappuccino']['ingredients']['water'])
        Coffee -= float(menu['cappuccino']['ingredients']['coffee'])
        Milk -= float(menu['cappuccino']['ingredients']['milk'])
        result = True
        return result
    elif Water < float(menu['cappuccino']['ingredients']['water']):
        print(f"Not enough water. Cappuccino requires {(menu['cappuccino']['ingredients']['water'])}ml\n"
              f"and there is only {Water}ml available. Please refill water.")
    elif Coffee < float(menu['cappuccino']['ingredients']['coffee']):
        print(f"Not enough coffee. Cappuccino requires {(menu['cappuccino']['ingredients']['coffee'])}g\n"
              f"and there is only {Coffee}g available. Please refill coffee beans.")
    elif Milk < float(menu['cappuccino']['ingredients']['milk']):
        print(f"Not enough milk. Cappuccino requires {(menu['cappuccino']['ingredients']['milk'])} ml,\n"
              f"and there is only {Milk}ml available.\nPlease refill milk.")

Water = 1000
Milk = 800
Coffee = 500
Money = 0

while True:
    user_choice = input(string_list[0])
    if user_choice.lower() == "report":
        report_check()
    elif user_choice.lower() == "espresso":
        user_cash = cash_app()
        dollar_convert()
        if espresso_check():
            money_check()
        else:
            print(f"{string_list[3]} ${dollars}")
    elif user_choice.lower() == "latte":
        user_cash = cash_app()
        dollar_convert()
        if latte_check():
            money_check()
        else:
            print(f"{string_list[3]} ${dollars}")
    elif user_choice.lower() == "cappuccino":
        user_cash = cash_app()
        dollar_convert()
        if cap_check():
            money_check()
        else:
            print(f"{string_list[3]} ${dollars}")
    elif user_choice.lower() == "exit":
        break
    else:
        print(string_list[2])
