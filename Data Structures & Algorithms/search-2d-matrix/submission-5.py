class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L = 0
        R = ROWS * COLS -1

        while L <= R:
            mid = (L+R) //2
            if matrix[mid//COLS][mid%COLS] == target:
                return True
            if matrix[mid//COLS][mid%COLS] < target:
                L = mid +1
            else:
                R = mid -1
        return False


