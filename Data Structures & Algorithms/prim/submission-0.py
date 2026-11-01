from collections import defaultdict
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for s, d, w in edges:
            adjList[s].append([d, w])
            adjList[d].append([s, w])
        visited = set()
        minHeap = list()
        for d, w in adjList[0]:
            heapq.heappush(minHeap, [w, 0, d])
        totalWeight = 0
        visited.add(0)
        while minHeap:
            w, s, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            totalWeight += w
            visited.add(n1)
            for n2, w in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [w, n1, n2])
        return -1 if len(visited) != n else totalWeight