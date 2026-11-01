class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf_object = UnionFind(n)

        for a, b in edges:
            uf_object.union(a, b)
        
        parents = set()
        
        for i in range(n):
            parents.add(uf_object.find(i))
        
        return len(parents)










        # DFS Solution
        # visited = set()
        # edgesMap = defaultdict(list)
        # for a, b in edges:
        #     edgesMap[a].append(b)
        #     edgesMap[b].append(a)
        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for neighbours in edgesMap[node]:
        #         dfs(neighbours)
        # count = 0
        # for i in range(n):
        #     if i not in visited:
        #         count += 1
        #         dfs(i)
        # return count
