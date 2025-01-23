hoursWorked = float(input("Please enter the number of hours that youworked: "))
hourlyRate = float(input("Please enter your hourly rate: "))
totalEarnings = hoursWorked * hourlyRate
print(f"You earned ${totalEarnings:.2f} for {hoursWorked} hours of
work at ${hourlyRate:.2f}/hour.") # :.2f ensures that it is formatted to be 2 decimal places