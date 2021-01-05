# Counting Characters
text = "Happy Birthday"
output = text.count("a")
print(output)

# Lower Case
a = "HAPPY BIRTHDAY"
a = a.lower()
print(a)

# Upper Case
b = "happy brithday"
b = b.upper()
print(b)

# Capitalize the first word
c = "happy birthday"
c = c.capitalize()
print(c)

# Capital letter of every word
d = "happy birthday"
d = d.title()
print(d)

# Is e lower case
e = "e"
lower = e.islower()
print(lower)

# Is f upper case
f = "F"
upper = f.isupper()
print(upper)

# Is everything in the text letters
g = "Happy Birthday"
text = g.isalpha()
print(text)

# Is everything a digit
h = "12345"
number = h.isdigit()
print(number)

# Is everything alpha numeric
i = "happybirthday123"
numeric = i.isalnum()
print(numeric)

# Search for a piece of text
j = "Happy Birthday"
piece = j.index("Birthday")
print(piece)

k = "Happy Birthday"
find = k.find("Birthday")
print(find)


# Strip a piece of text
l = "00000HappyBirthday00000"
strip = l.strip("0")
print(strip)

ls = "00000HappyBirthday0000"
lstrip = ls.lstrip("0")
print(lstrip)

rs = "00000HappyBirthday0000"
rstrip = rs.rstrip("0")
print(rstrip)

# To strip all the spaces from either side
m = "000000HappyBirthday00000"
spaces =m.strip()
print(spaces)

m_name = input("What is your name? ")#.strip()
print(m_name)


