# type: ignore

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # find the number that breaks the non-decreasing order from the right

        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # i = index of first number from the right that breaks the non-decreasing order
        # nums[i] < nums[i + 1]
        if i == -1:
            nums.reverse()
            return
        
        # find smallest number greater than i at the right side of i
        j = len(nums)-1
        while nums[j] <= nums[i]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]

        i = i + 1
        j = len(nums)-1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


