#
# https://leetcode.com/problems/set-matrix-zeroes/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.
#
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def zeroMatrix(matrix, n, m):
            row = [0] * n  # row array
            col = [0] * m  # col array

            # Traverse the matrix:
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] == 0:
                        # mark ith index of row wih 1:
                        row[i] = 1

                        # mark jth index of col wih 1:
                        col[j] = 1

            # Finally, mark all (i, j) as 0
            # if row[i] or col[j] is marked with 1.
            for i in range(n):
                for j in range(m):
                    if row[i] or col[j]:
                        matrix[i][j] = 0

            return matrix


# if __name__ == "__main__":
# 	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        n = len(matrix)
        m = len(matrix[0])
        ans = zeroMatrix(matrix, n, m)

        # print("The Final matrix is:")
        for row in ans:
            for ele in row:
                print(ele, end=" ")
            print()
