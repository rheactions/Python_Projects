#so we want to break the list and make it reverse
# arr = [1,2,3,4,5,6,7,8,9]
#expected arr = [3,2,1,6,5,4,9,8,7]
from intersection_of_list import result

arr = [1,2,3,4,5,6,7,8,9]
k = 3

chunks = [arr[i:i+k] for i in range(0,len(arr),k)]
print(chunks)

#reverse the chunks

reverse_chunks = [chunk[::-1] for chunk in chunks]
print(reverse_chunks)


result = []
for chunks in reverse_chunks:
    result.extend(chunks)

print(result)