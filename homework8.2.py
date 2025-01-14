import string

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Это не палиндром"))
print(is_palindrome("Madam, I'm Adam"))
