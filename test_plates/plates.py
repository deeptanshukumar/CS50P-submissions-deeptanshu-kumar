def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    char_statis = True if 2<=len(s)<=6 else False
    npsp = True if s.isalnum() else False
    number_not_in_middle = not_in_middle_checker(s+" ")
    if char_statis:
        char_2 = True if (s[0].isalpha() and s[1].isalpha()) else False
    else:
        char_2 = False
    if number_not_in_middle and char_statis and char_2 and npsp:
        return True
    else:
        return False


def not_in_middle_checker(string):
    numbers,number_after_number = [],True
    for i in string:
        if i.isdigit():
            numbers.append(i)
    if len(numbers)!=0 and numbers[0]!="0":
        for i in string:
            if i.isdigit():
                if (string[string.index(i)+1].isdigit()) or (string[string.index(i)+1]==" "):
                    number_after_number = True
                else:
                    number_after_number = False
                    break
        return number_after_number
    elif len(numbers)!=0 and numbers[0]=="0":
        return False
    return number_after_number


if __name__ == "__main__":
    main()

