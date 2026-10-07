class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        #treat as if a long 1D array len mxn
        L, R = 0, ROWS*COLS -1
        while L <=R:
            mid = (L+R) //2
            r, c = mid//COLS, mid%COLS
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                L = mid +1
            else:
                R = mid -1
        return False



        