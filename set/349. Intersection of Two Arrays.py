# type: ignore

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        res = set()
        for i in nums2:
            if i in s:
                res.add(i)
        
        return list(res)