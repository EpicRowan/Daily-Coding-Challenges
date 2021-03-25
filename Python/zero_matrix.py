''' Write an algorithm such that if an element 
	in an MxN matrix is 0,the entire row and column 
	are set to 0.'''

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)  
        n = len(matrix[0]) 
        rows = []
        cols = []
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    rows.append(x)
                    cols.append(y)

        def nullify_row(self, matrix, row):
            for i in range(len(matrix[0])):
                matrix[row][i] = 0

        def nullify_col(self, matrix, col):
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        for row in rows:
            nullify_row(self,matrix, row)

        for col in cols:
            nullify_col(self,matrix, col)

        return matrix