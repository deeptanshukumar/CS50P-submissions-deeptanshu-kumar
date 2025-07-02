balance,denominations = 50,[25,10,5]
while balance!=0:
    print(f"Amount Due: {balance}")
    money = int(input("Insert coin: "))
    if money in denominations:
        balance -= money
        print(f"Change Owed: {-1*balance}") if balance<=0 else print(f"Amount Due: {balance}")
