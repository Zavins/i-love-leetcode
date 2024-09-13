# type: ignore

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)

        # inductive: base case [n], n is a peak element.
        # we add another element k to form [n, k].
        # if k > n, then k is a peak element.
        # if k < n, then n ia still a peak element.
        # we always have 1 peak element.

        while l < r:
            mid = l + (r-l) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                # left neighbor greater
                # search left space
                r = mid
            elif mid < len(nums)-1 and nums[mid] < nums[mid + 1]:
                # right neighbor greater
                # search right space
                l = mid + 1
            else:
                # if mid is greater than both left and right, 
                # or mid = 0 and nums[mid] > nums[mid + 1], 
                # or mid = len(nums)-1 and nums[mid-1] < nums[mid]
                return mid