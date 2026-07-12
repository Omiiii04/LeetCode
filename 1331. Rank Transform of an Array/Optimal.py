class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        unique = sorted(set(arr))

        hashmap = {}

        for i, num in enumerate(unique):
            hashmap[num] = i + 1 

        return [hashmap[x] for x in arr]