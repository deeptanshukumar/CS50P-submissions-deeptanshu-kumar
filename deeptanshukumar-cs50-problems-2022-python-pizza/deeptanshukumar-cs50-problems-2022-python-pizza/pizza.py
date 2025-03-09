from tabulate import tabulate
import csv, sys

if len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-3:] == "csv":
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                table = reader.reader
                print(tabulate(table, headers=reader.fieldnames, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
