list = [12, 3, 4, 10]
list1 = (list [-1:] + list [:-1])
print (list, "=>", list1)

list1 = [1]
list2 = (list1 [-1:] + list1 [:-1])
print (list1, "=>", list2)

list3 = []
list4 = (list3 [-1:] + list3 [:-1])
print (list3, "=>", list4)

list5 = [12, 3, 4, 10, 8]
list6= (list5 [-1:] + list5 [:-1])
print (list5, "=>", list6)