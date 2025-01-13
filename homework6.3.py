def multiply_digits_until_single_digit(number):
    while number > 9:
        product = 1
        while number > 0:
            digit = number % 10
            product *= digit
            number //= 10
        number = product
    return number
if __name__ == "__main__":
    try:
        user_input = int(input("Введите целое число: "))
        if user_input < 0:
            print("Введите положительное число.")
        else:
            result = multiply_digits_until_single_digit(user_input)
            print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введено не целое число.")