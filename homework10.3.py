def is_even(number):
    """
    Проверяет, является ли число четным.

    :param number: Целое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0


print(is_even(4))  # True
print(is_even(7))  # False
print(is_even(0))  # True
