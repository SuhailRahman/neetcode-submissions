from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        edgesMap = defaultdict(list)

        for a, b in edges:
            edgesMap[a].append(b)
            edgesMap[b].append(a)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbours in edgesMap[node]:
                dfs(neighbours)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
