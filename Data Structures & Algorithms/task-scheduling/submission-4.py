from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task with highest count to go first
        # X2X
        # Y2Y

        # A3A3A

        # count would be at least n * max. + if there's any other with same count then + however many chars w same count. 
        counter = Counter(tasks)
        maxKeys = []
        maxCount = float("-inf")
        for key, count in counter.items():
            if counter[key] > maxCount:
                maxCount = counter[key]
            
        for key, count in counter.items():
            if counter[key] == maxCount:
                maxKeys.append(key)
        return max((maxCount + n*(maxCount-1) + len(maxKeys) -1), len(tasks))
        #    B
        # AB_AB_AB
        # A__A__A
        # AB_AB_AB
        # XY_XY