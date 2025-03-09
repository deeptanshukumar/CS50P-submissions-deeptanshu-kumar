def main():
    grocery_list = grocery_getter()
    list_printer(grocery_list)

def grocery_getter():
    grocery_list = {}
    try:
        while True:
            item = input().upper().strip()
            if item in grocery_list.keys():
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    except EOFError:
        print("")
        return grocery_list

def list_printer(grocery_list):
    for i in sorted(list(grocery_list.keys())):
        print(f"{grocery_list[i]} {i}")

main()
