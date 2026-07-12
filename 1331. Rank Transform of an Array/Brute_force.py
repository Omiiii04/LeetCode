class Solution:
    def rankArr(self, arr: List[int]) -> List[int]:

        sorted_arr = sorted(set(arr))

        for i in range(len(arr)):
            arr[i] = sorted_arr.index(arr[i]) + 1

        return arr
