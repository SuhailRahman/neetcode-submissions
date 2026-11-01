import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        freqMap = dict()

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1

        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            _, num = heapq.heappop(minHeap)
            res.append(num)
        
        return res

