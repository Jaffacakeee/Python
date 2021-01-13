# Unpacking
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(*numbers)
print(*"abc")

# Packing
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return (total)

# Unpacking keywords
def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and like{}".format(name, age, likes)
    return sentence

dictionary = {"name": "Ben", "age": 25, "likes": "Python"}
about(**dictionary)

# Packing keywords
def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))
foo(huda = "Female", Ben = "Male")