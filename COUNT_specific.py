#Write a Python function that counts
# how many times a specific character
# appears in a given string.
#from alphabet_counter import count

str = input("enter string: ")
empty_set = set()

for i in str:
    if i not in empty_set:

        print(f"{i}- {str.count(i)}")
        empty_set.add(i)

