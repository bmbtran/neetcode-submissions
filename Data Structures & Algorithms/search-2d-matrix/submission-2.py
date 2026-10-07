class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #[1,2,4,8,10,11,12,13,14,20,30,40]
        #R = 11
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, ROWS * COLS -1
        while L <= R:
            mid = (L + R)//2 #5
            row = mid // COLS #1
            col = mid % COLS #1
            if matrix[row][col] > target:
                R = mid - 1
            elif matrix[row][col] < target:
                L = mid + 1
            else:
                return True
        return False
#O(logn + logm) O(1)
#alternative:
#[1,3,5,7,10,11,16,20,23,30,34,60] 0, 11
#
