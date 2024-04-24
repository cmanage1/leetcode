import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs using level order traversal
        q = collections.deque([])
        if root:
            q.append(root)

        res = []

        while q:
            right = 0

            for _ in range(len(q)):
                node = q.popleft()
                right = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(right)

        return res
