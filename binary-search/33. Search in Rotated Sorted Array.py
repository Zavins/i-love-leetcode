# type: ignore
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the index (pivot) that left is > nums[-1] and right is <= nums[-1]
        pivot = self.find_pivot(nums)
        if target > nums[-1]:
            return self.bin_search(nums, target, 0, pivot)
        return self.bin_search(nums, target, pivot, len(nums))

    def find_pivot(self, nums):
        l = 0
        r = len(nums)
        target = nums[-1]

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > target:
                l = mid + 1
            else:
                r = mid
        return l

    def bin_search(self, nums, target, l, r):
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return -1