def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s)-1
    inputString = s.lower()
    while left<=right:
            if inputString[left]==inputString[right]:
                    left+=1
                    right-=1
            else:
                return False
            
    return True

print(is_palindrome("Madam")) # Output: True
print(is_palindrome("Hello")) # Output: False