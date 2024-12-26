#Write a function that accepts a list
# and an element as input and returns the
# index of the first occurrence of the element
# in the list. If the element does not exist,
# return -1.
from operator import indexOf


def give_index(list,element):

    if element in list:
        index =  list.index(element)
        return index
    else:
        return -1

list = eval(input("enter your list: "))
element = eval(input("enter your elemnent: "))

print(give_index(list,element))