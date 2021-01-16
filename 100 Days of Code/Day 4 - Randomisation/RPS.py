import random

rock = '''
     ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
     SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
user_choice = int(input("Pick a number: 0 - Rock, 1 - Paper, 2 - Scissors: "))
print(images[user_choice])

computer_choice = random.randint(0, 2)
print(images[computer_choice])


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
elif computer_choice > user_choice:
    print("You Lose")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Its a draw!")

