from collections import deque as queue
class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.BFS(grid, i, j)
                    count += 1
        return count

    # Function to check if a cell
    # is be visited or not
    def isValid(self, grid, row, col):

        # If cell lies out of bounds
        if (row < 0 or col < 0 or col >= len(grid[0]) or row >= len(grid) or grid[row][col] != '1'):
            return False

        # Otherwise
        return True

    # Function to perform the BFS traversal
    def BFS(self, grid, row, col):
        # Direction vectors
        dRow = [ -1, 0, 1, 0]
        dCol = [ 0, 1, 0, -1]
        
        # Stores indices of the matrix cells
        q = queue()

        # Mark the starting cell as visited
        # and push it into the queue
        q.append(( row, col ))

        # Iterate while the queue
        # is not empty
        while (len(q) > 0):
            cell = q.popleft()
            x = cell[0]
            y = cell[1]

            #q.pop()

            # Go to the adjacent cells
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if (self.isValid(grid, adjx, adjy)):
                    q.append((adjx, adjy))
                    grid[adjx][adjy] = "#"  
            
