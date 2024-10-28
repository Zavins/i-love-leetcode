# type: ignore

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        d = Deque([[]])
        l = 0
        r = 0

        queue = Deque([(root, 0)])
        while queue:
            node, position = queue.popleft()
            if node is None:
                continue
            if position == l - 1:
                l = l - 1
                d.appendleft([node.val])
            elif position == r + 1:
                r = r + 1
                d.append([node.val])
            else:
                d[position - l].append(node.val)
            queue.append((node.left, position - 1))
            queue.append((node.right, position + 1))
            
        return list(d)