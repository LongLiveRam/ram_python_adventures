email = input("Please enter your email: ")

print(
    f"Your username is {email[:email.index("@")]} and your domain is {email[email.index("@") + 1:]}")
