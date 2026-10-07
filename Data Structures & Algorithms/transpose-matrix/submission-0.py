class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #O(n*m) O(n*m)  
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0] * ROWS for _ in range(COLS)]
        for r in range(ROWS ):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
        return res 