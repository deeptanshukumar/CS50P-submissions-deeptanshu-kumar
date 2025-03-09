import requests, sys, json

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            float_num = float(sys.argv[1])
            response = requests.get(
                "https://api.coindesk.com/v1/bpi/currentprice.json"
            ).json()
            print(f"${response["bpi"]["USD"]["rate_float"]*float_num:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Too many arguments")

except requests.RequestException:
    print("Couldn't reach servers...")
