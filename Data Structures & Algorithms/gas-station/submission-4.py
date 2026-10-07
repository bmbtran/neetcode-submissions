class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #or there's no solution
        if sum(gas) - sum(cost) <0:
            return -1
        #either there's a solution
        # 1,-3,1,-2,3
        currGas = 0
        res= 0
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                res = i+ 1
                currGas = 0
        return res
        