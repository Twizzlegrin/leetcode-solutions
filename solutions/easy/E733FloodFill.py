from typing import List
"""
1. Initialize a function 'fill' that takes in the image, starting row, starting column, color to fill, and current color
2. Check if the starting row or column is out of bounds of the image
    If: return
3. Check if the current color is not equal to the color at the starting row and column
    If: return
4. Update the color at the starting row and column to the new color
5. Recursively call the 'fill' function on the 4 adjacent cells
6. Initialize the 'floodFill' function that takes in the image, starting row, starting column, and color to fill
7. Check if the color at the starting row and column is equal to the color to fill
    If: return the image
8. Call the 'fill' function on the image, starting row, starting column, color to fill, and current color
9. Return the image
"""

class Solution:
    def fill(self, image, sr, sc, color, cur):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return

        if cur != image[sr][sc]:
            return

        image[sr][sc] = color

        self.fill(image, sr + 1, sc, color, cur)
        self.fill(image, sr - 1, sc, color, cur)
        self.fill(image, sr, sc + 1, color, cur)
        self.fill(image, sr, sc - 1, color, cur)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color: return image

        self.fill(image, sr, sc, color, image[sr][sc])

        return image
