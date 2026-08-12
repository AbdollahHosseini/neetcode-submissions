class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1

        least = float('inf')

        paths = [[grid[m][n], m, n]]

        while paths:
            curr, m, n = paths.pop(0)
            if m == n and not n: 
                if curr < least:
                    least = curr
            else:
                if m > 0:
                    val1 = grid[m - 1][n]
                    paths.append([curr + val1, m - 1, n])
                
                if n > 0:
                    val2 = grid[m][n - 1]
                    paths.append([curr + val2, m, n - 1])
                    
            
        return least
            

