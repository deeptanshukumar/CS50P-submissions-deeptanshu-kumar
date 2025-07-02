def main():
    input_user = input("Input: ")
    print(shorten(input_user))

def shorten(user_input):
    vowels = ["a","e","i","o","u"]
    string_output = ""
    for i in user_input:
        if i in vowels:
            pass
        else:
            string_output += i
    return f"Output: {string_output}"

if __name__ == "__main__":
    main()
