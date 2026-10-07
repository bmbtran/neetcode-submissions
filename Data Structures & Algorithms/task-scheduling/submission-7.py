class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        maxf= 0
        total = 0
        for t in tasks:
            if t not in count:
                count[t] = 0
            count[t] +=1
        maxCount = 0
        for c in count.values():
            maxCount = max(c, maxCount)
        alsoMax = 0
        for c in count.values():
            if c == maxCount:
                alsoMax +=1
        total = max((maxCount -1) *(n+1) + alsoMax, len(tasks))
        return total

