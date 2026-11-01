# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_value_index_hashmap = dict()
        for idx, val in enumerate(inorder):
            inorder_value_index_hashmap[val] = idx
        self.pre_idx = 0
        def build(l, r):
            if l > r or r >= len(preorder):
                return None
            parentValue = preorder[self.pre_idx]
            self.pre_idx += 1
            p = TreeNode(parentValue)
            pIndex = inorder_value_index_hashmap[parentValue]
            p.left = build(l, pIndex-1)
            p.right = build(pIndex+1, r)
            
            return p

        # def build(preorderList, inorderList):
        #     if len(inorderList) == 0 or len(preorderList) == 0:
        #         return None
        #     parentValue = preorderList[0]
        #     p = TreeNode(parentValue)
        #     pIndex = inorderList.index(parentValue)
        #     if inorderList[0] != preorderList[0]:
        #         p.left = build(preorderList[1:pIndex+1], inorderList[:pIndex])
        #     if (pIndex + 1) < len(inorderList) and inorderList[pIndex+1] != preorderList[0]:
        #         p.right = build(preorderList[pIndex+1:], inorderList[pIndex+1:])
            
        #     return p
        
        return build(0, len(inorder)-1)