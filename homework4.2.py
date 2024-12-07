list = [0, 1, 7, 2, 4, 8]
sum_odd_index_elements = sum(list[i] for i in range(0, len(list), 2))
a = sum_odd_index_elements * list[-1]
print(a)

list1 = [1, 3, 5]
sum_odd_index_elements1 = sum(list1[i] for i in range(0, len(list1), 2))
a1 = sum_odd_index_elements1 * list1[-1]
print(a1)

list2 = [6]
sum_odd_index_elements2 = sum(list2[i] for i in range(0, len(list2), 2))
a2 = sum_odd_index_elements2 * list2[-1]
print(a2)

list3 = []
sum_odd_index_elements3 = sum(list3[i] for i in range(len(list3)))
a3 = sum_odd_index_elements3 * 0
print(a3)
