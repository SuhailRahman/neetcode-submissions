class UnionSet:
    def __init__(self, n):
        self.rank = {}
        self.p = {}
        for i in range(n):
            self.rank[i] = 1
            self.p[i] = i
    
    def find(self, u):
        p = self.p[u]
        while p != self.p[p]:
            p = self.p[self.p[p]]
        self.p[u] = p
        return self.p[u]
    
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.p[p2] = p1
            self.rank[p1] += self.rank[p2]
            self.rank[p2] = 1
        
        else:
            self.p[p1] = p2
            self.rank[p2] += self.rank[p1]
            self.rank[p1] = 1
        return True 


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adj_list = {node: [] for node in range(n)}

        # for n1, n2 in edges:
        #     adj_list[n1].append(n2) 
        #     adj_list[n2].append(n1)

        us_obj = UnionSet(n)

        for n1, n2 in edges:
            if not us_obj.union(n1, n2):
                return False
        p1 = us_obj.find(0)
        for node in range(n):
            if us_obj.find(node) != p1:
                return False

        return True
        
