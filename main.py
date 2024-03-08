print("\033c")
# import modules that we'll need 
from data import resources
from data import MENU
# Ask the user what they would like
money = 0

def is_resource_sufficient(order_ingredients):
    """Returns True if order can be made, returns false if it cant"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_coins():
    """Returns the calculated coins inserted"""
    print("Please insert coins.")
    # Get user input of how many coins they have 
    amt_quarters = float(input("how many quarters?: "))
    amt_dimes = float(input("how many dimes?: "))
    amt_nickels = float(input("how many nickels?: "))
    amt_pennies = float(input("how many pennies?: "))
    # Worth of coins 
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    # Calculation of amount of coins user inputed
    amt_quarters *= quarters
    amt_dimes *= dimes
    amt_nickels *= nickels 
    amt_pennies *= pennies
    money = amt_quarters + amt_dimes + amt_nickels + amt_pennies
    return money


def is_transaction_successful(money_recieved, drink_cost):
    """Return true when the payment is accepted or False if it's not"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False




def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name}")





is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"${money}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])



