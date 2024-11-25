user_number = input ("Введите 5-ти значное число: ")
num = int (user_number)
num1 = num % 1000
div, mod = divmod (num1, 10)
print (mod, end="")
num2 = num % 100
div, mod = divmod (num2, 10)
print (div, end="")
num3 = num // 100
div, mod = divmod (num3, 10)
print (mod, end="")
num4 = num // 1000
div, mod = divmod (num4, 10)
print (mod, end="")
num5 = num // 1000
div, mod = divmod (num4, 10)
print (div, sep="")
print ("Спасибо")