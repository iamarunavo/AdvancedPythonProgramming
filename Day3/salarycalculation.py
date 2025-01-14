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
