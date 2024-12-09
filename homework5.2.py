while True:
    user_number1 = int(input ("Введите 1-е число: "))
    user_number2 = int(input ("Введите 2-е число: "))
    user_action = input ("Введите действие с числами: (+, -, *, /): ")
    if user_action == "+":
        print ("Ваш ответ: ", user_number1 + user_number2)
    if user_action == "-":
        print ("Ваш ответ: ", user_number1 - user_number2)
    if user_action == "*":
        print ("Ваш ответ: ", user_number1 * user_number2)
    if user_action == "/":
        print("Ваш ответ: ", user_number1 / user_number2) if user_number2 != 0 else print("Деление на ноль невозможно!")
    again = input("Желаете продолжить?Нажмите 'y', Если нет,нажмите 'n': ")
    if again != 'y':
        print("Работа завершена!")
        break
