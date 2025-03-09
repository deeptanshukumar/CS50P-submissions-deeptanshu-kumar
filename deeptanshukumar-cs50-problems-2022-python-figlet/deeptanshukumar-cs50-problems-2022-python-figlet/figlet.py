import sys, random, pyfiglet
list_of_available_fonts = pyfiglet.Figlet().getFonts()
def main():
    match len(sys.argv):
        case 3:
            if sys.argv[1].lower() in ["-f","--font"]:
                if sys.argv[2] in list_of_available_fonts:
                    writer(sys.argv[2])
                else:
                    sys.exit(1)
            else:
                sys.exit(1)
        case 1:
            writer(random.choice(list_of_available_fonts))
        case _:
            sys.exit(1)


def writer(font_py):
    ascii_art = pyfiglet.figlet_format(input("Input: "), font=font_py)
    print("Output: "+ascii_art)

main()

