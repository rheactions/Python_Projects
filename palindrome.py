# b = "Hello, World!"
# print(b[2:5])


#Write a function that reverses every word in a sentence while keeping the order of words intact.
#sentence = "hello world python"
#"olleh dlrow nohtyp"

sentence = "hello world python"
# list_sen = list(sentence) converting string to list
# print(list_sen)
#s = ''.join(char_list)  # Converts back to "hello"

#but for above you'll need to use word split

# split_word = sentence.split() # splitthe word n word is ['Hello','word','python']
# j = [] # to append the reverse words in here
#
# for i in split_word:
#     y = i[::-1] # this will reverse every word
#
#     j.append(y)
#     print(j)
#
# joined_word = ' '.join(j)
# print(joined_word)


#reverse the sentence
# reversed_1 = sentence[::-1]
# print(reversed_1) #o/p nohtyp dlrow olleh
# sentence = "hello world python"
# split_word = sentence.split()
# split_word.reverse()
# joined = ' '.join(split_word)
# print(joined)

split = sentence.split()
y = []
for i in split:
    j = i[::-1]
    y.append(j)

s = ' '.join(y)
print(s)


