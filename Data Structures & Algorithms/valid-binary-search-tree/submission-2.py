# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def maxTreeNodeVal(subroot, maxValue):
        #     if not subroot:
        #         return maxValue
        #     return max(maxValue, subroot.val, maxTreeNodeVal(subroot.left, maxValue), maxTreeNodeVal(subroot.right, maxValue))
            
        # def minTreeNodeVal(subroot, minValue):
        #     if not subroot:
        #         return minValue
        #     return min(minValue, subroot.val, maxTreeNodeVal(subroot.left, minValue), maxTreeNodeVal(subroot.right, minValue))
        
        # if not root:
        #     return True
        
        # maxLeftVal = maxTreeNodeVal(root.left, float("-inf"))
        # minRightVal = minTreeNodeVal(root.right, float("inf"))

        # if root.val < maxLeftVal or root.val > minRightVal:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        

        def validateBST(root, left, right):
            if not root:
                return True
            
            if root.val <= left or root.val >= right:
                return False
            
            return validateBST(root.left, left, root.val) and validateBST(root.right, root.val, right)


        return validateBST(root, float("-inf"), float("inf"))
        