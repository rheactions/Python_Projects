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




# Summary Table of Iterations
# Iteration	left	right	s[left]	s[right]	Action Taken
# 1	        0	     10	     h	     d	        Move both
# 2	        1	     9	     e	     l	        Move right
# 3	        1	     8	     e	     r	        Move right
# 4	        1	     7	     e	     o	        Swap → "holle world"
# 5	        2	     6	     l	     w	        Move left
# 6	        3	     6	     l	     w	        Move left
# 7	        4	     6	     e	     o	        Swap → "hollo werld"
# 8	        5	     5	     Space	 Space	    Stop loop

