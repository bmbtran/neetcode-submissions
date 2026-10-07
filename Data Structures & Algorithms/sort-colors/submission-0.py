class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0] #red, white, blue o(1)
                #0,1,2
        #first pass: update the count array
        i = 0
        for num in nums:
            count[num] += 1 #count = [1,2,1]
                                    #0,1,2
        #second pass: dump those vals into nums array
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i +=1


        #for sorting, i know we can use mergesort, quicksort, insertion sort, and bucket sort. 
        