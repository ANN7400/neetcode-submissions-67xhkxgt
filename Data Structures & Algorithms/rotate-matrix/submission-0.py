class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            # j starts from i so we only traverse the upper triangle, 
            # avoiding swapping elements back to their original positions.
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()