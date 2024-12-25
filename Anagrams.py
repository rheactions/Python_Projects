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
