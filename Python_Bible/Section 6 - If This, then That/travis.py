known_users = ["Ben", "Chloe", "Natalie", "Peter", "Thomas"]

while True:
    print("Hello, my name is Travis.")
    name = input("What is your name? ").strip().lower().capitalize()

    if name in known_users:
        print("Hello {}.".format(name))
        remove = input("Would you like to be removed from the list (y/n)? ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("OK")
    else:
        add_name = input("Would you like to be added to the list (y/n)? ").strip().lower()

        if add_name == "y":
            known_users.append(name)
        elif add_name == "n":
            print("No problem")
            
