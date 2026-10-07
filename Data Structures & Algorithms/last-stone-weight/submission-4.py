class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #build max heap of size 2
        #if x == y pop both
        #pop smaller and larger = larger - smaller
        import heapq 
        stones = [-stone for stone in stones]
        maxHeap = stones
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, x-y)
        return abs(maxHeap[0]) if maxHeap else 0

