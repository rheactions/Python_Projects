# write a program to remove puntuations from the input string

string = input("Enter your string : ")

#we take an empty string
cleaned_text = ""


    # we wanna iterate through the string , for us to remove the punctuations
for text in string:
    if text.isalnum() or text.isspace():
        cleaned_text += text
print(cleaned_text)

#isalnum is a string method , which checks the string
#if it is either numbers or letters , then it returns True else False
#for eg if string is "Hello Riya" -> so there's a space in there which will make the return false
#for eg if the string is "Hello!" -> return false

#isspace method is for checking whether the string consists entirely of whitespace characters
#it returns true if string contains whitespaces

# print("    ".isspace())  # True (all spaces)
# print("\t".isspace())    # True (tab is considered whitespace)
# print("\n".isspace())    # True (newline is considered whitespace)
# print("Hello".isspace()) # False (not only whitespace)
# print("Hello world".isspace())  # False (contains letters)
