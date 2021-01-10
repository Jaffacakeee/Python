def about(name, age, likes = "Python"):
    sentence = "Meet {} he is {} years old and they like {}." .format(name, age, likes)
    return sentence

# 3 positional arguments
about("Jack", 23, "Python")

# 3 arguments with keywords
about(name = "Jack", age = 23, likes = "Python")

# Process an argument without all parameters, add likes = "Python" in parameters
about("Jack", 23)
