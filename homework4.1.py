items = [0, 1, 0, 12, 3]
a = [i for i in items if i != 0]
b= [i for i in items if i == 0]
c = a + b
print(items," => ",c)

items2 = [0]
if len(items2) <=1:
    print(items2,"=>",items2)
else:
    a1 = [i for i in items2 if i !=0]
    b1 = [i for i in items if i == 0]
    c1 = a1 + b1
    print(items2," => ",c1)

items3 = [1, 0, 13, 0, 0, 0, 5]
a2 = [i for i in items3 if i != 0]
b2 = [i for i in items3 if i == 0]
c2 = a2 + b2
print(items3," => ",c2)

items4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
a3 = [i for i in items4 if i != 0]
b3 = [i for i in items4 if i == 0]
c3 = a3+ b3
print(items4," => ", c3)
