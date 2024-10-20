# type: ignore

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if (val:=self.count_bst(root)) > -1:
                return val

            return max(dfs(root.left), dfs(root.right))
        return dfs(root)

    def count_bst(self, root, small = float('-inf'), large = float('inf')):
        if root is None:
            return 0

        if root.val <= small or root.val >= large:
            #if not valid, return -1
            return -1
        
        left = self.count_bst(root.left, small, root.val)
        right = self.count_bst(root.right, root.val, large)

        if left == -1 or right == -1:
            return -1
        return left + right + 1