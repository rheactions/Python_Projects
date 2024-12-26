
#Write a function that takes a string as input
# and counts how many vowels and consonants are in the string. Consider a, e, i, o, u as vowels, and all other alphabetic characters as consonants.

input_string = input("enter string: ")
vowels = ['a','e','i','o','u']
#if in case he vowels list now contains both lowercase and uppercase vowel characters ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). This ensures that both lowercase and uppercase vowels are correctly counted.

def vowel_counter():
    vowel = 0
    constant = 0
    for i in input_string:
        if i.isalpha():
            if i.lower() in vowels:
                vowel += 1
            else:
                constant += 1


    print(f"{vowel} letters are vowels")
    print(f"{constant} letters are constant")


vowel_counter()

#code is almost correct but each chara that is not vowel is
#being considered as constant i.e space or punctuatiosn
# for that use i.alpha()

