def main():
    input_user = input("Input: ")
    print(shortener(input_user))

def shortener(user_input):
    vowels = ["a","e","i","o","u"]
    string_output = ""
    for i in user_input:
        if i.lower() in vowels:
            pass
        else:
            string_output += i
    return f"Output: {string_output}"

main()
