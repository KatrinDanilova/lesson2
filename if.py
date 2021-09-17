

age = input("Сколько вам лет? ")

if int(age) <= 18:
    print("Никаких сигарет!")
else:
    print("Вам синий или красный?")


team = input("What is your team name? ")
level = input("What is your team level? ")

if team == 'mistic':
    if int(level) > 5:
        print(f"Hi {team}!")
    else:
        print(f"Hi {team}! You need more level!")
elif team == 'gold':
    print(f"Hi {team}!")
else:
    print(f"Hi noname!")


