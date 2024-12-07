import random
list = [random.randint(3, 10) for i in range(random.randint(3, 10))]
new_list = [list[0],list[2],list[-2]]
print(list," => ",new_list)