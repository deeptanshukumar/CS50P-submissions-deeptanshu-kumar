def main():
    time = input("What time is it? ").strip()
    if 7<=convert(time)<=8:
        print("breakfast time")
    elif 12<=convert(time)<=13:
        print("lunch time")
    elif 18<=convert(time)<=19:
        print("dinner time")
    else:
        pass

def convert(time):
    converted = int(time.split(" ")[0].split(":")[0]) + (int(time.split(" ")[0].split(":")[1]))/60
    if "a.m" in time:
        return converted
    elif "p.m" in time:
        return 12 + converted
    else:
        return int(time.split(":")[0]) + int(time.split(":")[1])/60

if __name__ == "__main__":
    main()
