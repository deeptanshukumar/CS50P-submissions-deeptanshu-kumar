import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as before_file, open(sys.argv[2], "w") as after_file:
            fieldnames = ["first", "last", "house"]
            reader, writer = csv.DictReader(before_file), csv.DictWriter(after_file, fieldnames = fieldnames)
            writer.writeheader()
            for row in reader:
                name, house = row["name"].split(", "), row["house"]
                writer.writerow({
                    "first": name[1],
                    "last": name[0],
                    "house": house
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
