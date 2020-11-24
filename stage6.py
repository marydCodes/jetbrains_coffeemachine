class Drink:
    recipe = {"water": 0,"milk": 0,"beans": 0,"money": 0}

    def __init__(self, water, milk, beans, money):
        self.recipe["water"] = water
        self.recipe["milk"] = milk
        self.recipe["beans"] = beans
        self.recipe["money"] = money

    def buy_it(self):
        for key in state.recipe:
            if Machine().state[key] < state.recipe[key]:
                return f"Sorry, not enough{key}!"
            print("I have enough resources, making you a coffee!")
            # update Machine() state according to drink??

class Machine:
    resource = {"water": 400, "milk": 540,"beans": 120,"money": 550, "cups": 9}
    state = "off"

    def __init__(self):
        print("~~~ Welcome ~~~")
    
    def fill(self):
        self.resource["water"] += int(input("Write how many ml of water do you want to add: "))
        self.resource["milk"] += int(input("Write how many ml of milk do you want to add: "))
        self.resource["beans"] += int(input("Write how many grams of coffee beans do you want to add: "))
        self.resource["cups"] += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
        print(f"I gave you ${self.resource['money']}")
        self.resource["money"] = 0

    def remaining(self):
        print(f'''
        The coffee machine has:
        {self.resource["water"]} ml of water
        {self.resource["milk"]} ml of milk
        {self.resource["beans"]} g of coffee beans
        {self.resource["cups"]} disposable cups
        ${self.resource["money"]} dollars of money''')

    def buy(self):
        coffee = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        
        if coffee == "1":
            espresso = Drink(250, 0, 16, 4)
            espresso.buy_it()
    
    def exit(self):
        print("Goodbye")
        self.state = "off"


machine = Machine()
user_input = str(input("Write action (buy, fill, take, remaining, exit): "))
# while user_input != "exit": # causes infinite loop though...
if machine.state == "buy":
    machine.buy()

elif user_input == "fill":
    machine.fill()

elif user_input == "take":
    machine.take()

elif user_input == "remaining":
    machine.remaining()
    user_input
# machine.exit()