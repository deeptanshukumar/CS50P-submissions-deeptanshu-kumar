import inflect
p = inflect.engine()

names = []
try:
    while True:
        name = input("Name: ").strip()
        if name=="":
            break
        else:
            names.append(name)
except EOFError:
    pass

print(f"Adieu, adieu, to {p.join(names)}")
