from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].split(".")[1].lower() in ["jpg", "jpeg", "png"]:
    if sys.argv[1].split(".")[1].lower() == sys.argv[2].split(".")[1].lower():
        try:
            with Image.open(sys.argv[1]) as before, Image.open("shirt.png") as shirt:
                size = shirt.size
                before = ImageOps.fit(before, size)
                before.paste(shirt, box = (0, 0), mask = shirt)
                before.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("Input and output have different extensions")
else:
    sys.exit("Invalid input")
