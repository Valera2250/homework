def format_time(seconds):
    if not (0 <= seconds < 8640000):
        print("Число должно быть больше или равно 0 и меньше 8640000.")
        return
    days, remainder = divmod(seconds, 86400)  # В одном дне 86400 секунд
    hours, remainder = divmod(remainder, 3600)  # В одном часе 3600 секунд
    minutes, seconds = divmod(remainder, 60)  # В одной минуте 60 секунд
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дня"
    else:
        day_word = "дней"
    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(formatted_time)
try:
    user_input = int(input("Введите число секунд (от 0 до 8639999): "))
    format_time(user_input)
except ValueError:
    print("Пожалуйста, введите целое число.")