class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f"Hello, I am {self.name}!")

# first = str(input())
# me = Person(first)
# me.greet()

############################################################

import math as m

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        return round(((3 * m.sqrt(3) * (self.side_length ** 2)) / 2), 3)

############################################################

class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        x_sq = (self.x - point.x) ** 2
        y_sq = (self.y - point.y) ** 2
        return m.sqrt(x_sq + y_sq)

# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
# print(p1.dist(p2))

############################################################

# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, dest):
        return f"The {self.name} has sailed for {dest}!"

# black_pearl = Ship("Black Pearl", 800)
# going_where = str(input())
# print(black_pearl.sail(going_where))

############################################################

class Lightbulb:
    def __init__(self):
        self.state = "off"

    def change_state(self):
        if self.state == "off":
            print("Turning the light on")
            self.state = "on"
        elif self.state == "on":
            print("Turning the light off")
            self.state = "off"

# test_light = Lightbulb()
# print("Start: ", test_light.state)
# test_light.change_state()
# print("changed once: ", test_light.state)
# test_light.change_state()
# print("changed twice: ", test_light.state)

############################################################

class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        # mark up deposit_cents
        if self.cents + deposit_cents > 99:
            self.dollars += (self.cents + deposit_cents) // 100
            self.cents = (self.cents + deposit_cents) % 100
        else:
            self.cents += deposit_cents

# bank = PiggyBank(1, 1)
# print(bank.dollars)
# print(bank.cents)

# bank.add_money(500, 500)
# print(bank.dollars, bank.cents)

############################################################

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

############################################################