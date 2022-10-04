import stuff


def order_req_check(context, ):
    global order
    depleted_resources = []
    if stuff.resources['water'] >= stuff.MENU[context]['ingredients']['water'] and stuff.resources['milk'] >= \
            stuff.MENU[order]['ingredients']['milk'] and stuff.resources['coffee'] >= \
            stuff.MENU[order]['ingredients']['coffee']:

        cost = stuff.MENU[context]["cost"]
        print(f'That will be ${cost}')
        quarters = 0.25 * float(input("How many quarters?: "))
        dimes = 0.10 * float(input("How many dimes?: "))
        nickles = 0.05 * float(input("How many nickles?: "))
        pennies = 0.01 * float(input("How many pennies?: "))

        money_in = quarters + nickles + dimes + pennies

        if money_in >= cost:

            stuff.resources['water'] -= stuff.MENU[context]['ingredients']['water']
            stuff.resources['milk'] -= stuff.MENU[order]['ingredients']['milk']
            stuff.resources['coffee'] -= stuff.MENU[order]['ingredients']['coffee']

            change = round(money_in - cost, 3)

            stuff.resources["money"] += money_in - change
            print(f"Your change is ${change} \nEnjoy your {context} :D")
        else:
            print("Insufficient funds")
    else:
        for resource in stuff.resources:
            if resource == "money":
                break
            else:
                if stuff.resources[resource] < stuff.MENU[context]["ingredients"][resource]:
                    depleted_resources.append(resource)
        print(f"Sorry, we are out of {' and '.join(depleted_resources)}")


shutdown = False

while not shutdown:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    while order not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        print('Not a valid input')
        order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'off':
        shutdown = True
    elif order == 'report':
        print(stuff.resources)
    else:
        order_req_check(order)
