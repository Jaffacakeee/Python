# Ask user for name
name = input("What is your name? ")

# Ask user for age
age = input("What is your age? ")

# Ask user for city
city = input ("What city do you live in? ")

# Ask user for what they love
love = input("What do you love? ")

# Build the structure of the sentence
string = "Your name is {} and you are {} old. You live in {} and love {}."
output = string.format(name, age, city, love)

# Print out sentence
print(output)
