class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # minHeap [0,1:1, 2:2, 3:3] num: freq sort by freq
        #build a minHeap size k [1:1, 2:2, 3:3]
        import heapq
        count = defaultdict(int)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        minHeap = []
        for n, freq in count.items():
            heapq.heappush(minHeap, (freq, n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for freq, n in minHeap:
            res.append(n)
        return res

