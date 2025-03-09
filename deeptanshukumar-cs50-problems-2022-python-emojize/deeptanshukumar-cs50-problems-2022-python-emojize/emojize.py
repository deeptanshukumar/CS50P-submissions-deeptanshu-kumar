import emoji
def emojizer(user_input):
    emojized = emoji.emojize(user_input, language='alias')
    return "Output: "+emojized

print(emojizer(input("Input: ")))

