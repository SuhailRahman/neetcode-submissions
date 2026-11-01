# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float("-inf")
        def pathSum(root, cur_sum):
            nonlocal max_sum
            if not root:
                return 0
            
            left = max(0, pathSum(root.left, cur_sum))
            right = max(0, pathSum(root.right, cur_sum))
            cur_sum = max(0, cur_sum)
            sum_including_root_left_right = cur_sum + root.val + left + right
            cur_sum = max(cur_sum + root.val, cur_sum + root.val + left, cur_sum + root.val + right)
            max_sum = max(max_sum, cur_sum, sum_including_root_left_right)
            return cur_sum
        
        pathSum(root, 0)
        return max_sum
        # def dfs(root):
        #     nonlocal max_sum
        #     if not root:
        #         return
        #     max_sum = max(max_sum, pathSum(root, 0))
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        # return max_sum
