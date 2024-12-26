from cffi.ffiplatform import flatten

#Given a list that may contain sublist,
# write a Python function that flattens
# it into a single list.
# For example, [[1, 2], 3, [4, [5, 6]]]
# should be flattened to [1, 2, 3, 4, 5, 6].

def flatten_list(input_list):
    flattened = []
    for item in input_list:
        if isinstance(item,list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

input_list = [1,2,3,[2,3]]
print(flatten_list(input_list))



