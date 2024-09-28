sets = {1, 21, 46, 94, 32, 47}
sets.add(99)
lists = [23, 67, 99, 42, 34, 89]
sets2 = set(lists)
sets.update(sets2)
print(sets)
even_nos = {0, 2, 4, 6, 8, }
odd_nos = {1, 3, 5, 7, 9, }
prime_nos = {1, 3, 5, 7, }
print(even_nos.union(odd_nos))
print(even_nos.intersection(odd_nos))
print(odd_nos.intersection(prime_nos))
print(odd_nos.difference(even_nos))
print(prime_nos.difference(even_nos))
print(even_nos.symmetric_difference(prime_nos))
#print(odd_nos.difference_update(prime_nos))
print(prime_nos.intersection_update(odd_nos))
print(prime_nos)
print(odd_nos)
set_list = {3, 6, 9, 12, 15, 18, 24}
set_list2 = {3, 9, 15, 27, 81, 102}
set_list3 = {3, 6, 9, }
set_list4 = {4, 20, 87, 23}
print(set_list3.issubset(set_list))
print(set_list2.isdisjoint(set_list4))
print(set_list.issuperset(set_list3))
set_list.symmetric_difference_update(set_list2)
print(set_list)
#To copy the contents of another set
set_list_copy = set_list.copy()
#Frozen set are immutable but are in line with other logical functions such as issdijoint, issubset etc
