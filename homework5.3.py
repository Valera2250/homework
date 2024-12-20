user_input = input("Введите строку: ")
import string
space = ''.join(x for x in user_input if x not in string.punctuation)
row = space.split()
ht = '#' + ''.join(i.title() for i in row)
if len(ht) > 140:
    ht = ht[:-1]
print(user_input,"==>",ht)
