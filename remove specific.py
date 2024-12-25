#Write a Python function that removes all
# occurrences of a specified element from a
# list and returns the updated list.
# Ensure the original list remains unchanged.
#from intersection_of_list import list1

def remove_element(input_list,element_to_remove):

    updated =[]

    for item in input_list:
        if item != element_to_remove:
            updated.append(item)

    return updated


input_list = eval(input("enter list:"))
print(remove_element(input_list,1))


