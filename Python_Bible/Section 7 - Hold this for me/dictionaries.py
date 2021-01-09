# Creating a dictionary with the names and ages of students, printing out the value of Dan
student = {"Alice": 25, "Bob":27, "Claire": 17, "Dan": 21, "Chloe": 22}
name = student["Dan"]
print(name)

# Creating a new name and value to add to the dictionary
student["Fred"] = 25

# Change the value of a name
student["Alice"] = 26

# Delete a name from a dictionary
del student["Fred"]

# Making a list out of the keys dictionary
a = list(student.keys())
print(a[1])

# Making a list of the values
b = list(student.values())
print(b)

# List all of the items within the dictionary
c = student.items()
print(c)

# Add multiple data to students & to get 1 part
second_student = {
                    "Alice":  ["ID0001", 26, "A"],
                    "Bob":    ["ID0002", 27, "B"],
                    "Claire": ["ID0003", 17, "C"],
                    "Dan":    ["ID0004", 21, "D"],
                    "Chloe":  ["ID0005", 22, "E"]
                 }
print(second_student["Claire"][0])
print(second_student["Dan"][1:])

# Add a dictionary in a dictionary
third_student = {
                    "Alice":  {"ID": "ID0001", "Age": 26, "Grade": "A"},
                    "Bob":    {"ID": "ID0002", "Age": 27, "Grade": "B"},
                    "Claire": {"ID": "ID0003", "Age": 17, "Grade": "C"},
                    "Dan":    {"ID": "ID0004", "Age": 21, "Grade": "D"},
                    "Chloe":  {"ID": "ID0005", "Age": 22, "Grade": "E"},
                 }
print(third_student["Dan"]["Age"])
print(third_student["Chloe"]["ID"], third_student["Chloe"]["Grade"])
