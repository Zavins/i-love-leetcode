# type: ignore

class Solution:
    # This algorithm only finds the min number, does not find the pivot.
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                # the smaller numbers are on the right part
                l = mid + 1
            elif nums[mid] < nums[r]:
                # the smaller number are on the left part, change r, so r is new target respect to the part.
                r = mid
            else:
                # move r / remove duplicates on the right side.
                r -= 1
        
        return nums[l]