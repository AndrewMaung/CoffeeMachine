import time
MENU = {
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

def money_calculation(quarters,dimes,nickel,penny):
    """ quarters = 25 cent
    dimes = 10 cent
    nickel = 5 cent
    penny = 1 cent"""
    
    quarters_converted = quarters * 25
    dimes_converted = dimes * 10
    nickel_converted = nickel * 5
    penny_converted = penny * 1
    
    total_amount = quarters_converted + dimes_converted + nickel_converted + penny_converted
    amt_dollars = float(total_amount / 100)
    return amt_dollars
    
def process(coffee_price):
    print("Please insert coins.")
    quarters = float(input("How many quarters:"))
    dimes = float(input("How many dimes:"))
    nickels = float(input("How many nickels:"))
    penny = float(input("How many penny:"))
    inserted_amt = money_calculation(quarters,dimes,nickels,penny)
    print("You have inserted" , inserted_amt , "dollars")
    change_amt = float(inserted_amt - coffee_price)
    rounded_change = float(round(change_amt,2))
    if inserted_amt < coffee_price:
        print("Please Insert Enough Money")
    else:
        print("Here is your change $", rounded_change) 
    
def resources_calculation(water, milk, coffee):
    if resources["water"] < water or resources["milk"] < milk or resources["coffee"] < coffee:
        print("Sorry, not enough resources to make this coffee. Try another option.")
        return False
    else:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        return True

    
while True:
    user_input = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        for key in resources:
            amount = resources[key]
            print(f"{key} : {amount}")
            
    elif user_input == "espresso":
        coffee_price = MENU["espresso"]["cost"]
        coffee_resources_water = MENU["espresso"]["ingredients"]["water"]
        coffee_resources_coffee = MENU["espresso"]["ingredients"]["coffee"]
        resources_calculation(coffee_resources_water,0,coffee_resources_coffee)
        process(coffee_price)

    elif user_input == "latte":
        coffee_price = MENU["latte"]["cost"]
        coffee_resources_water = MENU["latte"]["ingredients"]["water"]
        coffee_resources_milk = MENU["latte"]["ingredients"]["milk"]
        coffee_resources_coffee = MENU["latte"]["ingredients"]["coffee"]
        resources_calculation(coffee_resources_water,coffee_resources_milk,coffee_resources_coffee)
        process(coffee_price)
        
    elif user_input =="cappuccino":
        coffee_price = MENU["cappuccino"]["cost"]
        coffee_resources_water = MENU["cappuccino"]["ingredients"]["water"]
        coffee_resources_milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee_resources_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        resources_calculation(coffee_resources_water,coffee_resources_milk,coffee_resources_coffee)
        process(coffee_price)
        
    elif user_input == "exit":
        print("Exiting the Vending Machine", end="")
        for _ in range(5):
            time.sleep(1)
            print(".", end="", flush=True)  
        print()
        print("Have a nice day")
    
    else:
        print("Please Enter A Valid Input")