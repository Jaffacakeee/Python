from random import choice

questions = ["Why is the sky blue? ",
             "Who am I? ",
             "Why day is it tomorrow? "
            ]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ")

print("Oh... Okay")
