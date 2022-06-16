from constants import MENU, resources, COIN_VALUES

total_money_in_machine = 0


def any_resources_insufficient(option):
    insufficient_ingredient = ""
    for resource in resources:
        if resource in MENU[option]["ingredients"] and MENU[option]["ingredients"][resource] > resources[resource]:
            insufficient_ingredient = resource.capitalize()
            break
    return insufficient_ingredient


def deduct_resources(option):
    for resource in resources:
        if resource in MENU[option]["ingredients"]:
            resources[resource] = resources[resource] - MENU[option]["ingredients"][resource]


def coffee_machine():
    global total_money_in_machine

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if not choice == "off":
        if choice == "report":
            for resource in resources:
                print(f"{resource.capitalize()}: {resources[resource]} ml")
            print(f"Money: $ {total_money_in_machine}")

        elif choice in MENU and any_resources_insufficient(choice) == "":
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = round(((COIN_VALUES["quarters"] * quarters) + (COIN_VALUES["dimes"] * dimes) + (
                    COIN_VALUES["nickels"] * nickels) + (COIN_VALUES["pennies"] * pennies)), 2)
            price_of_drink = MENU[choice]["cost"]
            change = round((money_inserted - price_of_drink), 2)

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")

                total_money_in_machine += price_of_drink
                deduct_resources(choice)

        elif not any_resources_insufficient(choice) == "":
            print(f"Sorry! There is not enough {any_resources_insufficient(choice)}.")

        else:
            print("Please enter a valid option.")

        coffee_machine()
    else:
        print("Good bye!")


coffee_machine()
