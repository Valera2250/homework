def find_unique_value(numbers):
    for number in numbers:
        if numbers.count(number) == 1:
            return number
    return None

print(find_unique_value([1, 2, 2, 3, 3]))
print(find_unique_value([4, 5, 6, 5, 4]))
print(find_unique_value([7, 7, 7]))
