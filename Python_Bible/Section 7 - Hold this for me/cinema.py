films = {
            "Finding Dory":  {"Age": 3, "Tickets": 5},
            "Bourne":        {"Age": 18, "Tickets": 5},
            "Tarzan":        {"Age": 12, "Tickets": 5},
            "Ghost Busters": {"Age": 15, "Tickets": 5},
        }
print("========= MOVIES-SHOWING =========")
while True:
    choice = input("What film would you like to see? ").strip().title()

    if choice in films:
        age = int(input("How old are you? ").strip())
        if age >= films[choice]["Age"]:
            num_seats = films[choice]["Tickets"]
            if num_seats > 0:
                print("Enjoy the film.")
                films[choice]["Tickets"] = films[choice]["Tickets"] - 1
                print("{} tickets remaining for that film.".format(films[choice]["Tickets"]))
                print("==================================")
            else:
                print("Sorry we are sold out of tickets for that film.")
        else:
            print("Sorry you are too young for {}".format(choice))
    else:
        print("Sorry we are not showing {}".format(choice))


