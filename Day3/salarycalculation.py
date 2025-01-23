hoursWorked = float(input("Enter number of hours worked: "))
hourlyRate = float(input("Enter hourly rate: "))
# straight hours is capped at at 40 if overtime
straightHours = (hoursWorked <= 40) * hoursWorked + (hoursWorked >
40) * 40
overtimeHours = (hoursWorked > 40) * (hoursWorked - 40)
straightPay = straightHours * hourlyRate
overtimePay = overtimeHours * (1.5 * hourlyRate)
totalPay = straightPay + overtimePay
print(f"Straight pay: {straightPay:.2f}")
print(f"Overtime pay: {overtimePay:.2f}")
print(f"Total pay: {totalPay:.2f}")


#using stuff we haven't learned
'''
hoursWorked=float(input("Enter # of hours worked: "))
hourlyRate = float(input("Enter your hourly rate: "))
normalHours = 40
overtimeRate = 1.5
straightHours = min(hoursWorked, normalHours)
straightPay = straightHours * hourlyRate
overtimeHours = max(0, hoursWorked-40)
overtimePay = overtimeHours * hourlyRate * overtimeRate
totalPay = straightPay + overtimePay
print(f"StraightPay: ${straightPay:.2f}")
print(f"OvertimePay: ${overtimePay:.2f}")
print(f"TotalPay: ${totalPay:.2f}")

'''

