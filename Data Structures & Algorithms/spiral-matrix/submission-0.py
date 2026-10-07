class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #[0][0] -> [0][1] 
        #[0][1] -> [0][2]
        #[0][2] -> [1][2] (when j == len(matrix) -1, then we loop increment i )
        #[1][2] -> [2][2] 
        #[2][2] -> [2][1] (when i == len(matrix) -1 and j == len(matrix) -1, then j -=1 )
        #[2][1] -> [2][0]
        #[2][0] -> [1][0]
        #[1][0] -> [1][1] #handle differently add seen to hashset
        #if seen then turn right -> increment j +1
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []
        while left < right and top < bottom:
            #traverse top
            for i in range(left, right):
                res.append(matrix[top][i])
            top +=1
            #traverse right
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -=1
            #check if condition still satisfied
            if not (left < right and top < bottom):
                break
            #traverse bottom
            for i in range(right -1, left -1, -1):
                res.append(matrix[bottom -1][i])
            bottom -=1
            #traverse left
            for i in range(bottom -1, top -1, -1):
                res.append(matrix[i][left])
            left +=1

        return res


