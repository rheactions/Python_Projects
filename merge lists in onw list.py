#Given two sorted lists,
# write a Python function that merges them into a single sorted list.
#
# The result should contain all the elements from both
# lists in ascending order.

l1 = [4,2,3]
l2 = [3,6,1]

def sorted_merge(l1,l2):
    l3 = sorted(l1) + sorted(l2)
    print(sorted(l3))

sorted_merge(l1,l2)