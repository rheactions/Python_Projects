#Write a Python function that takes two lists and
# returns a new list containing only the elements
# that appear in both lists. The order of elements
# in the result should follow the order they appear in the first list.


list1 = [1,2,4,3,1]
list2 = [1,2,4,32,2]

result = []

for i in list1:
    if i in list2:
        result.append(i)
        list2.remove(i)

print(result)