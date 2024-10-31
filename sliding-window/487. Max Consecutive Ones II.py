# type: ignore

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        flip = 1

        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flip -= 1
            
            while flip < 0:
                if nums[l] == 0:
                    flip += 1
                l += 1
            
            res = max(res, r -l + 1)
        
        return res
