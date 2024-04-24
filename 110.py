# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # what is height balanced?
        # depth of every 2 subtrees never differ by more than one
        # hints at some sort of dfs
        # track height per both subtrees

        def dfs(root, height):
            if not root:
                return True, 0
            else:
                leftBalanced, leftHeight = dfs(root.left, height+1)
                rightBalanced, rightHeight = dfs(root.right, height+1)
                
                balanced = leftBalanced and rightBalanced and abs(leftHeight-rightHeight) <= 1
                height = 1 + max(leftHeight, rightHeight)

                return balanced, height 

        return dfs(root, 0)[0]
