class Book:
    material = "paper"
    cover = "paperback"
    all_books = []

class Elf:
    height = 1.8
    weapon = "longbow"
    emotional_maturity = 125

#print(Book.material)

#anElf = Elf()
#print(anElf.emotional_maturity)

class RockBand:
    genre = "rock"
    key_instruments = ["electric guitar", "drums"]
    n_members = 4

#two_per = RockBand()
#print(two_per.genre)
#print(two_per.n_members)
#print(two_per.key_instruments)

class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = round(((1/2) * (leg_1 * leg_2)), 1)


# triangle from the input
# input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
# c_square = input_c ** 2
# eqnR = (input_a ** 2) + (input_b ** 2)
# if c_square == eqnR:
#     triangle = RightTriangle(input_c, input_a, input_b)
#     print(triangle.area)
# else:
#     print("Not right")

class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + birth_year

# first = str(input())
# last = str(input())
# byear = str(input())
# a_student = Student(first, last, byear)
# print(a_student.student_id)

class Movie:

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

#titanic = Movie("Titanic", "James Cameron", 1997)
#star_wars = Movie("Star Wars", "George Lucas", 1977)
#fight_club = Movie("Fight Club", "David Fincher", 1999)

class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = (4 / 3) * self.PI * (radius ** 3)

class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

t = str(input())
a = str(input())
y = str(input())

stuff = Painting(t, a, y)
print(f'"{stuff.title}" by {stuff.painter} ({stuff.year}) hangs in the {stuff.museum}.')