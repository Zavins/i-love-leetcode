# type: ignore

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums)-1
        curr = r

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[curr] = nums[l]**2
                l += 1
            else:
                res[curr] = nums[r] ** 2
                r -= 1
            curr -= 1
        return res