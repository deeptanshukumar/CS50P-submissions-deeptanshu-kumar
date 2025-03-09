x,y,z = input("Expression: ").strip().split(" ")
def interpretor(int(x),y,int(z)):
    if y == "/":
        if z==0:
            print("Z cant be zero!")
        else:
            print(f"{(x/z):.1f}")
    else:
        match y:
            case "+":
                print(f"{(x+z):.1f}")
            case "-":
                print(f"{(x-z):.1f}")
            case "*":
                print(f"{(x*z):.1f}")
            case _:
                print("unrecognized input")

interpretor()
