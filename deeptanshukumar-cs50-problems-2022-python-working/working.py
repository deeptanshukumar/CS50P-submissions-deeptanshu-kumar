import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        pattern = r"^([0-9]|1[0-2])((:[0-5][0-9])| ?) (AM|PM) to ([0-9]|1[0-2])((:[0-5][0-9])| ?) (AM|PM)$"
        match = re.search(pattern, s, re.IGNORECASE)
        new_list = list(match.groups())
    except AttributeError:
        raise ValueError("invalid input")

    hour1, minutes1, hour2, minutes2, ampm1, ampm2 = (
        new_list[0],
        new_list[1],
        new_list[4],
        new_list[5],
        new_list[3],
        new_list[7],
    )
    h1, h2 = time_24(int(hour1), ampm1, int(hour2), ampm2, minutes1, minutes2)
    if minutes1 == "" and minutes2 == "":
        return f"{h1:02}:00 to {h2:02}:00"
    elif minutes1 == "" and minutes2 != "":
        return f"{h1:02}:00 to {h2:02}{minutes2}"
    elif minutes1 != "" and minutes2 == "":
        return f"{h1:02}{minutes1} to {h2:02}:00"
    else:
        return f"{h1:02}{minutes1} to {h2:02}{minutes2}"


def time_24(hour1, ampm1, hour2, ampm2, minutes1, minutes2):
    if (
        (minutes1 == "" or 0 <= int(minutes1[1:]) <= 59)
        and (minutes2 == "" or 0 <= int(minutes2[1:]) <= 59)
        and 1 <= hour1 <= 12
        and 1 <= hour2 <= 12
        and ampm1 != ampm2
    ):
        if ampm1.lower() == "am":
            if hour1 == 12:
                hour1, hour2 = 0, 12
            elif hour2 == 12:
                pass
            else:
                hour2 += 12
        else:
            if hour2 == 12:
                hour2, hour1 = 0, 12
            elif hour1 == 12:
                pass
            else:
                hour1 += 12

        return [hour1, hour2]
    else:
        raise ValueError("Time given is invalid!")


if __name__ == "__main__":
    main()
