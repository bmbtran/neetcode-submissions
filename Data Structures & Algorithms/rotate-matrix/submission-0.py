class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = COLS = len(matrix)
        #reverse
        matrix.reverse()
        #transpose
        for r in range(ROWS):
            for c in range(r, COLS):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp


