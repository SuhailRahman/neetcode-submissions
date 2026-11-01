# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kSmallest(root):
            nonlocal k, res
            if not root:
                return
            kSmallest(root.left)
            if k == 0:
                return
            k -= 1
            if k == 0:
                res = root.val
                return
            kSmallest(root.right)
        res = root.val
        kSmallest(root)
        return res
