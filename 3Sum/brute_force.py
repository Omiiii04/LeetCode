class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sum = 0
        new_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == sum:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in new_list:
                            new_list.append(triplet)

        return new_list