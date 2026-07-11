class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        solution = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i -1]:
                continue

            l = i + 1 
            r = len(nums) -1
            
            while l < r:
                c_sum = num + nums[l] + nums[r]

                if c_sum == 0:
                    ele = nums[i], nums[l], nums[r]
                    
                    solution.append(ele)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1

                elif c_sum < 0:
                    l += 1

                else:
                    r -= 1

        return solution