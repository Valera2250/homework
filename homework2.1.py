user_number = input ("Введите 4-х значное число: ")
num = int (user_number)
print ("Ваше число: ")
num1 = num // 100
div, mod = divmod (num1, 10)
print (div)
print (mod)
num3 = num % 100
div, mod = divmod (num3, 10)
print (div)
print (mod)
print ("Спасибо!")