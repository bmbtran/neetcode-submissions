import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #maxHeap
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            last = heapq.heappop(maxHeap)
            secondLast = heapq.heappop(maxHeap)
            if last < secondLast:
                heapq.heappush(maxHeap, last-secondLast)
        maxHeap.append(0)
        return abs(maxHeap[0])
