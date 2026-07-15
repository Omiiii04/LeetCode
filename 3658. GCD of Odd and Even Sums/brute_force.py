class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        odd_sum = 0
        even_sum = 0

        for i in range(1,(n + n + 1)):
            if i % 2 == 0:
                even_sum += i
            else:
                odd_sum += i
        
        gcd = 1

        for i in range(1, min(odd_sum, even_sum) + 1):
            if odd_sum % i == 0 and even_sum % i == 0:
                gcd = i

        return gcd
        