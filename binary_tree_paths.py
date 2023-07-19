# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def helper(root, string):
            if not root.left and not root.right:
                ans.append("->".join(string))
            if root.left:
                string.append(str(root.left.val))
                helper(root.left, string)
                string.pop()
            if root.right:
                string.append(str(root.right.val))
                helper(root.right, string)
                string.pop()
        if root:
            helper(root, [str(root.val)])
        return ans
