# Get user email address
email = input("What is you email address? ").strip()

# Slice out username
username = email[:email.index("@")]

# Slice out domain name
domain = email[email.index("@") + 1 :]

# Format Message
output = "Your username is: {}, and your domain is: {}".format(username, domain)

# Display output message
print(output)
