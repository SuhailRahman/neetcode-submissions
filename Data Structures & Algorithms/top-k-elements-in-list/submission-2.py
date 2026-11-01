import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # minHeap = []
        # freqMap = dict()

        # for num in nums:
        #     if num not in freqMap:
        #         freqMap[num] = 0
        #     freqMap[num] += 1

        # for num, freq in freqMap.items():
        #     heapq.heappush(minHeap, (freq, num))
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        # res = []
        # for i in range(k):
        #     _, num = heapq.heappop(minHeap)
        #     res.append(num)
        
        # return res

        freqMap = dict()

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            arr = bucket[i]
            for num in arr:
                res.append(num)
                if len(res) == k:
                    return res
        return res


