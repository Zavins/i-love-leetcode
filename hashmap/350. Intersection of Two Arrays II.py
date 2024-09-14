# type: ignore

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = Counter(nums1)
        map2 = Counter(nums2)
        res = []
        for k, v1 in map1.items():
            v2 = map2.get(k, 0)
            res.extend([k]*min(v1, v2))
        
        return res