
#create a empty dictionary

dict = {}

string = input("enter your word : ")

def alpha_counter(string):

    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    return dict


dict = alpha_counter(string)
#print(dict)

for char,count in dict.items():
    if char != " ":

        print(char,'-',count)
