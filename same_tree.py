# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None or q is None and p is not None:
            return False
        elif p is None and q is None:
            return True
        elif p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
