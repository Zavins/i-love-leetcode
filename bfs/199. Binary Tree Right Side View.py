# type: ignore

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        queue = Deque([root, None])
        prev = None
        while queue:
            node = queue.popleft()

            if node is None:
                res.append(prev.val)
                if queue:
                    queue.append(None)
            else:
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            prev = node
        
        return res