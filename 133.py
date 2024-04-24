import collections
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
        # deep clone of graph
        # do an iteration dfs or bfs, copy into copy
        if not node:
            return None

        graphCopy = {}

        def dfs(node):
            if node in graphCopy:
                return graphCopy[node]

            copy = Node(node.val)
            graphCopy[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)
