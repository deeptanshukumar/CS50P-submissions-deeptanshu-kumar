import random


def main():
    level, score, q = get_level(), 0, 0
    while q != 10:
        numbers = generate_integer(level)
        ans = numbers[0] + numbers[1]
        user_answers = input(f"{numbers[0]} + {numbers[1]} = ")
        try:
            user_answer = int(user_answers)
        except ValueError:
            user_answer = user_answers
        if user_answer == ans:
            q += 1
            score += 1
        else:
            q += 1
            print("EEE")
            for i in range(2):
                new_user_answers = input(f"{numbers[0]} + {numbers[1]} = ")
                try:
                    new_user_answer = int(new_user_answers)
                except ValueError:
                    new_user_answer = new_user_answers
                if i == 1:
                    if new_user_answer == ans:
                        break
                    else:
                        print("EEE")
                        print(f"{numbers[0]} + {numbers[1]} = {ans}")
                        break
                if new_user_answer == ans:
                    break
                else:
                    print("EEE")

    print(f"score: {score}")


def get_level():
    while True:
        n = input("Level: ")
        if n.isdigit():
            if n in ["1", "2", "3"]:
                return int(n)
            else:
                pass
        else:
            pass


def generate_integer(level):
    if level == 1:
        return [random.randint(0, 9), random.randint(0, 9)]
    elif level == 2:
        return [random.randint(10, 99), random.randint(10, 99)]
    else:
        return [random.randint(100, 999), random.randint(100, 999)]


if __name__ == "__main__":
    main()
