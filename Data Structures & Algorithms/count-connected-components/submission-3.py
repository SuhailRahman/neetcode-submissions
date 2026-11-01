class UnionSet:
    def __init__(self, n):
        self.comp = n
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
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return
        self.comp -= 1

        if self.rank[p1] > self.rank[p2]:
            self.p[p2] = p1
            self.rank[p1] += self.rank[p2]
            self.rank[p2] = 1
        else:
            self.p[p1] = p2
            self.rank[p2] += self.rank[p1]
            self.rank[p1] = 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        us_obj = UnionSet(n)
        for n1, n2 in edges:
            us_obj.union(n1, n2)
        
        return us_obj.comp
        