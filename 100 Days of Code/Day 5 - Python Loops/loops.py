import random

## Looping through list to print out the list items
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#--------------------------------------------------------------------------------#

# ## Looping through a list to print out the final average of 2 sums
# student_height = input("Enter students heights: ").split()
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# print(student_height)
#
# total_height = 0
# for height in student_height:
#     total_height += height
# print(total_height)
#
# total_amount = 0
# for amount in student_height:
#     total_amount += 1
# print(total_amount)
#
# average = round(total_height / total_amount)
# print(average)
#--------------------------------------------------------------------------------#

# Highest score out of a list
# student_score = input("Enter students scores: ").split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
# print(student_score)
#
# score = 0
# for i in student_score:
#     if score < i:
#         score = i
# print(score)
#--------------------------------------------------------------------------------
# Adding all the even numbers up to 100
# even = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         even += number
# print(even)
#--------------------------------------------------------------------------------
# The FizzBuzz Job interview
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FIZZBUZZ")
#     elif number % 3 == 0:
#         print("FIZZ")
#     elif number % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number)
#--------------------------------------------------------------------------------
# Password Generator
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print('''

,----------------------------------------------------,
| [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |
|                                                    |
|  [][][][][][][][][][][][][][_]    [][][]  [][][][] |
|  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |
| [][_][][][][][][][][][][][][]||     []    [][][][] |
| [__][][][][][][][][][][][][__]    [][][]  [][][]|| |
|   [__][________________][__]              [__][]|| |
`----------------------------------------------------'
''')
print("------------------------------------------------------")
print("--------- WELCOME TO THE PASSWORD GENERATOR ----------")
print("------------------------------------------------------")
nr_letters = int(input("Enter amount of letters: ").strip())
nr_numbers = int(input("Enter amount of numbers: ").strip())
nr_symbols = int(input("Enter amount of symbols: ").strip())

password = [""]

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, nr_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char

for char in range(1, nr_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

random.shuffle(password)
result = "".join(password)
print("Your random password is: {}".format(result))
