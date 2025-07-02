def main():
    user_input = input("string: ")
    print(convert(user_input))

def convert(input_string):
    elements = input_string.split(" ")
    final_string = ""
    for i in elements:
        if i == ":)":
            final_string += "🙂 "
        elif i == ":(":
            final_string += "🙁 "
        else:
            final_string += i + " "
    return final_string

main()
