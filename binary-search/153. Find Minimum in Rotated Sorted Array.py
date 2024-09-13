# type: ignore

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # same as finding the number on pivot
        l = 0
        r = len(nums)
        target = nums[-1]

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]