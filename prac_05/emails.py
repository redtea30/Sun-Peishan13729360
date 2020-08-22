"""
CP1404/CP5632 - Practical
emails
"""
email_to_name = {}

email = input("Enter your email: \n> ")
while email != "":
    before_email = email.split("@")[0]
    name_parts = before_email.split(".")
    name = " ".join(name_parts).title()

    check = input("Is your name {0}? (Y/N) \n> ".format(name)).upper()
    if check != "Y" and check != "":
        name = input("Name: ")
    email_to_name[email] = name

    email = input("Enter your email: \n> ")


for email, name in email_to_name.items():
    print("{0} ({1})".format(name, email))
