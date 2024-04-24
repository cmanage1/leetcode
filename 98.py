# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, leftVal, rightVal):
            if not root:
                return True
            
            if not (rightVal > root.val and leftVal < root.val):
                return False

            return isValid(root.left, leftVal, root.val) and isValid(root.right, root.val, rightVal)

        return isValid(root, float("-inf"), float("inf"))
