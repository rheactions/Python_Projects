# Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.
#
#
# Input : s1 = "dad"
#         s2 = "bad"
# Output : The strings aren't anagrams.


s1 = input("enter s1 : ")
s2 = input("enter s2 : ")

def anagrams(s1,s2):

    if sorted(s1) == sorted(s2):
        print("Strings are anagrams")
    else:
        print("Not anagrams")

anagrams(s1,s2)


# Note the sorted func here returns a list

#Anagram: A word formed by rearranging the letters of another word (e.g., "listen" and "silent").
#Reversing: A word written backward, which does not necessarily form a valid or meaningful word (e.g., reversing "listen" gives "netsil").
#sorting genrally returns a list in ascending order
#what it would do in case of letters or alphabets would be that it would rearrange the letters in alphabetically order and compare them instead.
