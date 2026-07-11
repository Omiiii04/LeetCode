class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(numbers, start = 1 ):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i