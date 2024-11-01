# type: ignore

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        curr = float('-inf')
        for r in range(len(nums)):
            if nums[r] != curr:
                nums[l] = nums[r]
                curr = nums[l]
                l += 1
        
        return l