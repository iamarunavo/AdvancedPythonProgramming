def reverse_string1(x: str) -> str:
    reverse_str = x[::-1]
    return reverse_str

print(reverse_string1("Madam"))

def reverse_string2(x: str) -> str:
    reverse_str = "" 
    for i in range(len(x)-1, -1, -1):
        reverse_str += x[i]
    return reverse_str

print(reverse_string2("Madam"))

def one_upper(s: str) -> bool:
    upperCount = 0
    for char in s:
        if char.isupper():
            upperCount += 1
    return upperCount == 1

def all_upper(s: str) -> bool:
    return s == s.upper()

def clear(x):
    punctuation = [".", ",", ";"]
    for i in range(len(x)):
        for symbol in punctuation:
            if symbol in x[i]:
                x[i] = x[i].replace(symbol, "")
    return x

def count_ones(n: int) -> int:
    total_count = 0
    for i in range(1, n + 1):
        total_count += str(i).count('1')
    return total_count


