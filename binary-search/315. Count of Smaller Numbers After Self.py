# type: ignore

from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = SortedList()
        res = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            res[i] = l.bisect_left(nums[i])
            l.add(nums[i])
        
        return res