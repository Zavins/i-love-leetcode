# type: ignore

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bin_search(nums, target)
        right = self.bin_search(nums, target + 1) - 1

        if (
            0 <= left < len(nums)
            and nums[left] == target
            and 0 <= right < len(nums)
            and nums[right] == target
        ):
            return [left, right]
        return [-1, -1]

    def bin_search(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
