def is_even(number: int) -> bool:
    return (number & 1) == 0


print(is_even(2))   # True
print(is_even(3))   # False
print(is_even(100)) # True
print(is_even(-5))  # False
