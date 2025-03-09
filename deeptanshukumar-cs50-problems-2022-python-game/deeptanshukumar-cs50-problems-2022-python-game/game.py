import random

while True:
    try:
        level = int(input("Level: "))
        if level>=1:
            x = random.randint(1, level)
            while True:
                guess = int(input("Guess: "))
                if guess > x:
                    print("Too large!")
                elif guess < x:
                    print("Too small!")
                elif guess == x:
                    print("Just right!")
                    break
            break
        else:
            pass

    except ValueError:
        pass
