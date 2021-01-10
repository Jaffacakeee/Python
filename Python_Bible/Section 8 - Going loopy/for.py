# for loop, variable, key word in, itterable
for number in range(1, 11, 2):
    print(number)

for letter in "ABCD":
    print(letter)

# Prints out the number of cons and vowels in a piece of text
vowels = 0
cons = 0
for letters in "Hello Motherfuckers":
    if letters.lower() in "aeiou":
        vowels = vowels + 1
    elif letters in " ":
        pass
    else:
        cons = cons + 1
print("CONS {}, VOWELS {}".format(cons, vowels))

# how to use a for loop for dictionaries, prints names which only include A
students = {
            "male":     ["Tom", "Charlie", "Harry", "Frank"],
            "female":   ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
           }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

# List comprehensions
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print(odd_numbers)

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answers = [[w.upper(), w.lower(), len(w)] for w in words]
print(answers)
