# You want your program to work in a way that at any given time there can be no more than 10 puppies.
# Define __new__ method so that this restriction is placed on the class.

class Puppy:
    n_puppies = 0

    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(cls)

class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __str__(self):
        return f"{self.title} by {self.author}. ${self.price}. [{self.book_id}]"

class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return f"Object of the class Patient. name: {self.name}, last_name: {self.last_name}, age: {self.age}"

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"