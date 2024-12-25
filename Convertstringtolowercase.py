
#Write a function that converts a string
# to all lowercase letters.
# For example, "Hello World" should become
# "hello world".

string = input("enter string: ")
def lower_me(string):
    for i in string:
        print(i.lower(),end="")

lower_me(string)