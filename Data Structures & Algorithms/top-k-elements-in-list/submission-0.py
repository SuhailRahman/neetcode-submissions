import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        freqMap = dict()

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1

        for num, freq in freqMap.items():
            heapq.heappush(maxHeap, (-freq, num))
        res = []
        for i in range(k):
            _, num = heapq.heappop(maxHeap)
            res.append(num)
        
        return res

