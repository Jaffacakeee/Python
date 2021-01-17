import math

# # Simple Function
# def greet():
#     print("Hello Ben")
#     print("How do you do Ben?")
#     print("Isn't the weather nice today?")
# greet()
#
# # Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# greet_with_name("Ben")

# Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Ben", "Cannock")

# Function with keyword arguments
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with(name = "Ben", location = "Cannock")
#------------------------------------------------------------------------------------
# Painting a wall
# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)
#------------------------------------------------------------------------------------
# Prime Number Checker
def prime_checker(number):
    if n > 1:
        for i in range(2, n):
            if(n % i) == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")


n = int(input("Check this number: "))
prime_checker(number = n)
