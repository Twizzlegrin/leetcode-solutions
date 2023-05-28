from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        1. Initialize the 'max_area' variable to 0
        2. Iterate through the rows of the grid
        3. Iterate through the columns of the grid
        4. Check if the current cell is 1
            If: call the 'dfs' function on the grid, row, and column
        5. Return the 'max_area'
        """
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.dfs(grid, row, col))

        return max_area

    def dfs(self, grid, row, col):
        """
        1. Check if the row or column is out of bounds of the grid
            If: return 0
        2. Check if the current cell is 0
            If: return 0
        3. Update the current cell to 0
        4. Recursively call the 'dfs' function on the 4 adjacent cells
        5. Return 1 + the sum of the 4 recursive calls
        """
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0

        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0

        return 1 + self.dfs(grid, row + 1, col) + self.dfs(grid, row - 1, col) + self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)

