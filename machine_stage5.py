state = {"w": 400,
         "m": 540,
         "b": 120,
         "c": 9,
         "d": 550}

# recipe espresso
espresso = {"w": 250,"m": 0,"b": 16,"d": 4}

# recipe latte
latte = {"w": 350,"m": 75,"b": 20,"d": 7}

# recipe cappuccino
cappuccino = {"w": 200,"m": 100,"b": 12,"d": 6}

# process queries
# first ask if they want to buy, fill or take
def choose():
    user_input = str(input("Write action (buy, fill, take, remaining, exit): "))
    return user_input

def buy():
    coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if coffee == 1:
        # update state according to espresso
        state["w"] -= espresso["w"]
        state["m"] -= espresso["m"]
        state["b"] -= espresso["b"]
        state["c"] -= 1
        state["d"] += espresso["d"]
    elif coffee == 2:
        print("You chose a latte. Pretty standard.")
        # update state according to latte
        state["w"] -= latte["w"]
        state["m"] -= latte["m"]
        state["b"] -= latte["b"]
        state["c"] -= 1
        state["d"] += latte["d"]
    elif coffee == 3:
        print("You chose a cappuccino. Foamy!")
        # update state according to cappuccino
        state["w"] -= cappuccino["w"]
        state["m"] -= cappuccino["m"]
        state["b"] -= cappuccino["b"]
        state["c"] -= 1
        state["d"] += cappuccino["d"]


def fill():
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    state["w"] += add_water
    state["m"] += add_milk
    state["b"] += add_beans
    state["c"] += add_cups

def take():
    print(f"I gave you ${state['d']}")
    state["d"] = 0

def remaining():
    print(f'''
    The coffee machine has:
    {state["w"]} ml of water
    {state["m"]} ml of milk
    {state["b"]} g of coffee beans
    {state["c"]} disposable cups
    {state["d"]} dollars of money''')

def exit(): print("Goodbye")

def machine_on():
    user_input = choose()
    if user_input == "buy":
        buy()
    elif user_input == "fill":
        fill()
        machine_on()
    elif user_input == "take":
        take()
        machine_on()
    elif user_input == "remaining":
        remaining()
        machine_on()
    elif user_input == "exit":
        exit()

machine_on()