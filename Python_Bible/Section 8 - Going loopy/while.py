
# using increasing numbers to print out even numbers up to 10
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number = number + 1

# Adding names to a list using a while loop until its full
L = []
while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry list is full")
print(L)

