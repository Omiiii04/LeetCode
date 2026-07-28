class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        n = len(s)

        if n < 2:
            return s

        mid = n//2

        left = "".join(sorted(s[0:mid]))

        if n % 2 == 0:
            return left + left[::-1]
        else:
            return left + s[mid] + left[::-1]


'''
How I solved this problem:
    1. I first calculated this string's mid half as we know that a palindrome is symmetric, so we only need to sort the first half of the string.
    2. Sort the left half and mirror it if length is even else add mid element if odd length.
'''