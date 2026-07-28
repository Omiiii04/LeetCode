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