# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easiy call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#-------------------------------------------------------------------------------------
# student_scores = {
#     "Harry": 81
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
#
# student_grade = {}
#
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grade[student] = "Outstanding"
#     elif score > 80:
#         student_grade[student] = "Great"
#     elif score > 70:
#         student_grade[student] = "awesome"
#     else:
#         student_grade[student] = "fail"
#
# print(student_grade)
#-------------------------------------------------------------------------------------
# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# Nesting a list in a dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"]
# }
#
# # Nest dictionaries inside dictionaries
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
# }
#
# # Nesting Dictionary in a list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     }
# ]

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow, Saint Petersburg"])
print(travel_log)
