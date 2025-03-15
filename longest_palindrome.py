#Write a function that finds the longest palindromic
# substring in a given string. A palindrome is a string that
# reads the same forward and backward.



# class Solution:
#     def longestPalindrome(self,s):
#         res = ''
#         reslen = 0
#
#         for i in range(len(s)):
#             #odd length
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l +1) > reslen:
#                     res = s[l:r+1]
#                     reslen = r - l +1
#                 l -= 1
#                 r += 1
#
#             #evwe lengh
#             l, r = i, i +1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > reslen:
#                     res = s[l:r + 1]
#                     reslen = r - l + 1
#                 l -= 1
#                 r += 1
#
#         return res
#
# sol = Solution()
# print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(sol.longestPalindrome("cbbd"))   # Output: "bb"


def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i + len(longest), len(s)):  # Start from i + current longest length
            substring = s[i:j+1]
            if substring == substring[::-1]:
                longest = substring  # Update longest palindrome
    return longest

s = 'bananas'
print(longest_palindrome(s))