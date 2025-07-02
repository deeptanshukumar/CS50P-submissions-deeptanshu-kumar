from datetime import date
import inflect
import sys


def main():
    print(convert(input("Date of Birth: ")))

def convert(s):
    try:
        birthday = date.fromisoformat(s)
    except ValueError:
        sys.exit("Not a valid format.")

    today = date.today()
    min = (today-birthday).days * 24 * 60

    converter = inflect.engine().number_to_words
    return converter(min, andword="").capitalize()+" minutes"

if __name__ == "__main__":
    main()
