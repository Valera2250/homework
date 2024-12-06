lst = [1, 2, 3, 5, 6]
list1 = (len(lst) + 1) // 2
res = [lst[:list1],lst[list1:]]
print(lst," => ",res)

lst1 = [1, 2, 3]
list2 = (len(lst1) + 1) // 2
res1 = [lst1[:list2],lst1[list2:]]
print(lst1," => ",res1)

lst2 = [1, 2, 3, 4, 5]
list3 = (len(lst2) + 1) // 2
res2 = [lst2[:list1],lst2[list1:]]
print(lst2," => ",res2)

lst3 = [1]
list4 = (len(lst3) + 1) // 2
res3 = [lst3[:list1],lst3[list1:]]
print(lst3," => ",res3)

lst4 = []
list5 = (len(lst4) + 1) // 2
res4 = [lst4[:list1],lst4[list1:]]
print(lst4," => ",res4)