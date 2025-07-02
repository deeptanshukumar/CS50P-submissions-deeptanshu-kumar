def main():
    user_greeting = input("Greeting: ").strip().lower()
    if "hello" in user_greeting:
        amount(0)
    elif user_greeting[0] == "h":
        amount(20)
    else:
        amount(100)

def amount(money):
    print(f"${money}")

main()

