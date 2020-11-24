class Drink:
    recipe = {"water": 0,"milk": 0,"beans": 0,"money": 0}

    def __init__(self, water, milk, beans, money):
        self.recipe["water"] = water
        self.recipe["milk"] = milk
        self.recipe["beans"] = beans
        self.recipe["money"] = money

class Machine:
    resource = {"water": 400, "milk": 540,"beans": 120,"money": 550, "cups": 9}
    state = "off"

    def __init__(self):
        print("~~~ Welcome ~~~")
        self.state = "on"
    
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
        return coffee
        

# espresso, latte and capp as instances of class Coffee
latte = Drink(350, 75, 20, 7) # recipe dictionary populated on instantiation

on = Machine()
drink = on.buy()
print(drink)
