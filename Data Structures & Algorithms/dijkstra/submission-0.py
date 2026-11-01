from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = defaultdict(list)
        for sr, dest, weight in edges:
            adjList[sr].append([weight, dest])
        minHeap = list()
        minHeap.append([0, src])
        shortest = {}
        while minHeap:
            w1, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            
            for w2, neighbour in adjList[node]:
                heapq.heappush(minHeap, [w1+w2, neighbour])
            shortest[node] = w1
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
        

