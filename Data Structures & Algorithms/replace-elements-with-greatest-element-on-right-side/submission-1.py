class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # iterate backward
        # new max = max (oldmax, arr[i])
        greatest = -1
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            arr[i] = greatest
            greatest = max(curr, greatest)
        return arr