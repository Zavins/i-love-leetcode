# type: ignore

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = dict()

        def dfs(node):
            if node is None:
                return None
            if node in visited:
                return visited[node]
            newNode = Node(val = node.val)
            visited[node] = newNode
            newNode.neighbors = []

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            
            return newNode

        return dfs(node)