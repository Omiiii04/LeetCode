class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        first = second = 0

        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        return (first - 1) * (second - 1)


'''
How I solved it:
    1. I initially thought of sorting the array and then taking the last two elements to calculate the product. However, that would take O(n log n) time complexity.
    2. Instead, I realized that I can find the two largest numbers in a single pass through the array, which would take O(n) time complexity.   

'''