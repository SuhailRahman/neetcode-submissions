"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        visited = set()
        head = None
        q.append(node)
        hash_map = dict()
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node.val in hash_map:
                    new_node = hash_map[cur_node.val]
                else:
                    new_node = Node(cur_node.val)
                    hash_map[cur_node.val] = new_node
                if not head:
                    head = new_node
                neighbor_list = []
                for neighbor in cur_node.neighbors:
                    if neighbor.val not in hash_map:
                        q.append(neighbor)
                        tmp_node = Node(neighbor.val)
                        hash_map[neighbor.val] = tmp_node
                    neighbor_list.append(hash_map[neighbor.val])
                if neighbor_list:
                    new_node.neighbors = neighbor_list
                
        return head


        
        