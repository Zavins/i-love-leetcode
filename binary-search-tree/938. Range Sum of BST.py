# type: ignore

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def backtrack(node):
            if node is None:
                return 0
            res = 0
            if low <= node.val <= high:
                res += node.val

            if node.val < high:
                res += backtrack(node.right)
            
            if node.val > low:
                res += backtrack(node.left)

            return res
        
        return backtrack(root)
