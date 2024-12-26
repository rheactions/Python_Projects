#Write a Python function that counts the number of words in a
# sentence. Assume words are separated by spaces.

input_string = input("enter you string here: ")

def word_counter(input_string):
    counted = input_string.split()


    # so here we are just spliting the string by space separator
    #which is default value
    # you can also separate the string by
    #input_string.split(',')
    print(len(counted))

word_counter(input_string)