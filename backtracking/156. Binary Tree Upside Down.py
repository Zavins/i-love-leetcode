# type: ignore

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def recursive(node):
            if node.left is None:
                return node
            
            newroot = recursive(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = None
            node.right = None

            return newroot
        return recursive(root)
