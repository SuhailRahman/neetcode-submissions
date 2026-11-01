import heapq
class MedianFinder:

    def __init__(self):
        """
        Idea is to have maxHeap and minHeap, maxHeap is for 1st half of the numbers and minHeap is for rest. If maxHeap top element is greater than minHeap top element then heapify both by poping out elements
        """
        self.first_half = [] # maxHeap
        self.second_half = [] # minHeap
        self.first_len = 0
        self.second_len = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_half, num * -1)
        self.first_len += 1
        if self.second_len and (self.first_half[0]*-1) > self.second_half[0]:
            val = heapq.heappop(self.first_half) * -1
            heapq.heappush(self.second_half, val)
            self.first_len -= 1
            self.second_len += 1
        if (self.first_len - self.second_len) > 1:
            val = heapq.heappop(self.first_half) * -1
            heapq.heappush(self.second_half, val)
            self.first_len -= 1
            self.second_len += 1
        elif (self.second_len - self.first_len) > 1:
            val = heapq.heappop(self.second_half) * -1
            heapq.heappush(self.first_half, val)
            self.first_len += 1
            self.second_len -= 1
        

    def findMedian(self) -> float:
        count = self.first_len + self.second_len
        # print(self.first_half, self.second_half)
        if count % 2 == 0:
            median = ((self.first_half[0] * -1)+ self.second_half[0]) / 2
            return median
        else:
            if self.first_len > self.second_len:
                median = self.first_half[0]*-1
            else:
                median = self.second_half[0]
            return float(median)
        