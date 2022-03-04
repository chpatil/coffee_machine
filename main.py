TO_CONTINUE = True
MONEY=0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" :0
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

def resource_check(resource):
    if MENU[resource]["ingredients"]["water"]>resources["water"] :
        print("Sorry there is not enough water.")
        return False
    elif MENU[resource]["ingredients"]["milk"]>resources["milk"] :
        print("Sorry there is not enough milk.")
        return False
    elif MENU[resource]["ingredients"]["coffee"]>resources["coffee"] :
        print("Sorry there is not enough coffee.")
        return False
    else:
        return  True


def coin_manager(dimes , nickels , quarters,pennies,user_input):
    total=0.10*dimes+0.05*nickels+0.25*quarters+0.01*pennies
    if total<MENU[user_input]["cost"]:
        global MONEY
        MONEY += MENU[user_input]["cost"]
        return False
    else:
        print(f"Here is {round(total-MENU[user_input]['cost'],2)} in change.")
        return True

# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”




while TO_CONTINUE:
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if resource_check(user_input):
            print("Please insert coins.")
            dimes=int(input("how many dimes?:"))
            nickels=int(input("how many nickels?:"))
            quarters=int(input("how many quarters?: "))
            pennies=int(input("How many pennies?: "))
            if coin_manager(dimes, nickels, quarters, pennies, user_input):
                resources["water"] -= MENU[user_input]["ingredients"]["water"]
                resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
                print(f"Here is your {user_input} ☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_input=="report" :
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${MONEY}")
    elif user_input=="off":
        TO_CONTINUE=False
    else:
        print("Please enter proper option")


