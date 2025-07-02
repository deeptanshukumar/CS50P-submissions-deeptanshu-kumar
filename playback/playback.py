def main():
    user_string = input("")
    playback(user_string)
def playback(string_slower):
    words = string_slower.split(" ")
    print("...".join(words))

main()
