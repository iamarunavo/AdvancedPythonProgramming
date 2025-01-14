amount=float(input("Please enter an amount of money: "))
cents = round(amount * 100)

halfDollars = cents // 50
cents %= 50

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents // 1
cents %= 1

print(f"Amount of half dollar coins: {halfDollars}")
print(f"Amount of quarters: {quarters}")
print(f"Amount of dimes: {dimes}")
print(f"Amount of nickels: {nickels}")
print(f"Amount of pennies: {pennies}")
