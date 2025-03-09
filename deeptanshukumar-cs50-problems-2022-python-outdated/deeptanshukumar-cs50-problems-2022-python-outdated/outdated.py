months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    user_date = input("Date: ").strip()
    try:
        if user_date[0].isalpha():
            m,d,y = user_date.split(" ")
            if (m.title() in months) and ("," in d):
                m,d,y = int(months.index(m.title())+1), int(d.removesuffix(",")), int(y)
                if 1<=m<=12 and 1<=d<=31:
                    print(f"{y}-{m:02}-{d:02}")
                    break
        else:
            m,d,y = user_date.split("/")
            if 1<=int(m)<=12 and 1<=int(d)<=31:
                print(f"{int(y)}-{int(m):02}-{int(d):02}")
                break
    except ValueError:
        continue
