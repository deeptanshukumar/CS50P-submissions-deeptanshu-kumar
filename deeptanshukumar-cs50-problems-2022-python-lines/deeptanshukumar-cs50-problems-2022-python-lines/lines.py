import sys

if len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-2:] == "py":
        try:
            count = 0
            with open(sys.argv[1]) as file:
                for i in file.readlines():
                    if i.strip().startswith('#') or i.isspace():
                        pass
                    else:
                        count+=1
            print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
