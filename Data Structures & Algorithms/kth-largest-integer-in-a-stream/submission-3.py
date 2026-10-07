class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #min heap of size K
        #when larger than K then pop smallest one
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #if k < len(minHeap): 
        #just push
        #if not, then push, then pop smallest
        heapq.heappush(self.minHeap, val)
        if self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
