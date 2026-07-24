class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return len(nums)
        
        return 1 << len(nums).bit_length()