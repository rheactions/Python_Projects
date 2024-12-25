#Given two sorted lists,
# write a function that merges them
# into a single sorted list.
# The merged list should contain all elements
# from both lists in sorted order.


list1 = [2,3,5]
list2 =[3,4,56]

list1.extend(list2)
#The extend() method modifies the original list
# in place and does not return a new list.
# Instead, it returns None. So when you do
# list1 = list1.extend(list2), list1 ends up
# being None.
print(sorted(list1))