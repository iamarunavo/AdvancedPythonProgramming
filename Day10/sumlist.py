def int_add(x: str, y: str) -> str:
    if len(x) < len(y):
        padding = "0" * (len(y) - len(x))
        x = padding + x
    elif len(x) > len(y):
        padding = "0" * (len(x) - len(y))
        y = padding + y

    carry = 0
    result = ""

    for i in range(len(x) - 1, -1, -1):
        digitSum = int(x[i]) + int(y[i]) + carry
        result = str(digitSum % 10) + result
        carry = digitSum // 10

    if carry > 0:
        result = str(carry) + result

    return result