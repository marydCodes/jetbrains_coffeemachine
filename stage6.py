class Drink:
    recipe = {"water": 0, "milk": 0, "beans": 0}
    cost = 0

    def __init__(self, water, milk, beans, money):
        self.recipe["water"] = water
        self.recipe["milk"] = milk
        self.recipe["beans"] = beans
        self.cost = money

    def buy_it(self):
        for key in self.recipe:
            if machine.resource[key] < self.recipe[key]:
                return f"Sorry, not enough{key}!"
            print("I have enough resources, making you a coffee!")
            # update machine state according to drink??
        for key in self.recipe:
            machine.resource[key] -= self.recipe[key]
        machine.resource["money"] += self.cost
        machine.resource["cups"] -= 1


class Machine:
    resource = {"water": 400, "milk": 540, "beans": 120, "money": 550, "cups": 9}
    state = "off"

    def __init__(self):
        espresso = Drink(250, 0, 16, 4)
        latte = Drink(350, 75, 20, 7)
        capp = Drink(200, 100, 12, 6)
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
            espresso.buy_it()
        elif coffee == "2":
            latte.buy_it()
        elif coffee == "3":
            capp.buy_it()

    def exit(self):
        print("Goodbye")
        self.state = "off"


machine = Machine()
user_input = input("Write action (buy, fill, take, remaining, exit): ")
while user_input != "exit": # causes infinite loop though...
    if user_input == "buy":
        machine.buy()
    elif user_input == "fill":
        machine.fill()
    elif user_input == "take":
        machine.take()
    elif user_input == "remaining":
        machine.remaining()
    user_input = input("Write action (buy, fill, take, remaining, exit): ")
machine.exit()
