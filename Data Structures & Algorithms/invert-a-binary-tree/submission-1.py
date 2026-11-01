# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # DFS
        # if not root:
        #     return None
        # tmp_right = root.right
        # root.right = root.left
        # root.left = tmp_right
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # # BFS
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root