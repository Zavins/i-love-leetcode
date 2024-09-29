# type: ignore 

from collections import Counter

class Solution:
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    #     m = dict()
    #     res = 0
    #     for i in nums:
    #         if m.get(i, 0) > 0:
    #             res += m.get(i)
    #             m[i] += 1
    #         else:
    #             m[i] = 1
        
    #     return res
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for i in c.values():
            res += i * (i - 1) // 2

        return res
