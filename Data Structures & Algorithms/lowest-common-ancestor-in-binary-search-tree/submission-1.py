# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def buildAncestor(cur_root, node, ancestor_list):
        #     if not cur_root:
        #         return
        #     ancestor_list.append(cur_root)
        #     if cur_root.val == node.val:
        #         return
        #     elif node.val < cur_root.val:
        #         buildAncestor(cur_root.left, node, ancestor_list)
        #     else:
        #         buildAncestor(cur_root.right, node, ancestor_list)
        
        # p_parent = []
        # q_parent = []
        # buildAncestor(root, p, p_parent)
        # buildAncestor(root, q, q_parent)
        # for i in range(min(len(p_parent), len(q_parent))-1, -1, -1):
        #     if p_parent[i].val == q_parent[i].val:
        #         return p_parent[i]

        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
