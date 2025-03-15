# reverse the vowels in the strings
#expected = 'Holle werld'

#✅ Hint: Extract vowels → Reverse them → Place back using slicing.

def reverse_vowel(s):
    vowels = 'aeiouAEIOU'
    vowel_list = list(vowels)
    left,right = 0 , len(s) - 1

    while left < right :
        if s[left] not in vowel_list:
            left += 1
        elif s[right] not in vowel_list:
            right -=1
        else:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1

    return "".join(s)

s = input("enter a string: ")
print(reverse_vowel(s))






