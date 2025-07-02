def main():
    user_input = user_input_percent()
    fraction = fraction_convert(user_input)
    if fraction<=1:
        print("E")
    elif fraction>=99:
        print("F")
    else:
        print(f"{int(fraction)}%")

def user_input_percent():
    while True:
        fraction_user = input("Fraction: ")
        try:
            x,y = fraction_user.strip().split("/")
            x,y = int(x),int(y)
            if x<=y:
                return (x/y)*100
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

def fraction_convert(percent):
    if (percent%1)<0.5:
        return percent-(percent%1)
    else:
        return percent-(percent%1)+1
    
main()
