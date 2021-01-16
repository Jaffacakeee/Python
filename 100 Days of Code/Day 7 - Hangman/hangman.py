import random
from word_list import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

lives = 6
end_of_game = False
display = []
print(logo)

# Create blanks
for i in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Enter a letter: ").lower()
    if guess in display:
       print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOST!")

    if "_" not in display:
        end_of_game = True
        print("YOU WON!")

    print(stages[lives])