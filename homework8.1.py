def add_one(digits):
    number = int(''.join(map(str, digits)))
    number += 1
    return [int(digit) for digit in str(number)]
result = add_one([1, 2, 3, 4])
print(result)
