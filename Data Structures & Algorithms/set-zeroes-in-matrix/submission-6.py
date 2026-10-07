class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        xArr = [0]*ROWS
        yArr = [0]*COLS
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    xArr[i] = 1
                    yArr[j] = 1
        for i in range(ROWS):
            for j in range(COLS):
                if xArr[i] or yArr[j]:
                    matrix[i][j] = 0
        


        