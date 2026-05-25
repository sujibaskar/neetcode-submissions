
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])

        l,ri=0 ,r*c-1
        while l<=ri:
            m=l+(ri-l) //2
            row,col=m//c,m%c
            if target> matrix[row][col]:
                l=m+1
            elif target<matrix[row][col]:
                ri=m-1
            else:
                return True
        return False