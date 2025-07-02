import validators

def main():
    email = input("What's your email address? ")
    print(email_validator(email))


def email_validator(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

main()
