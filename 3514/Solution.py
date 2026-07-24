class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)

        prefinal = []
        final = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prefinal.append(nums[i] ^ nums[j])

        for i in prefinal:
            for num in nums:
                final.append(i ^ num)

        return len(list(set(final)))