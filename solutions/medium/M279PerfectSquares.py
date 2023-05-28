from collections import deque
import math


class Solution:
    """
    1. Initialize a queue with (n, 0) where 0 is the level and a visited set to keep track of visited numbers
    2. Initialize a list of squares from 1 to sqrt(n)
    3. Start a while loop with queue as the condition
        a. Pop the first element from the queue
        b. If the number is 0, return the level
        c. Iterate through the squares
            i. If the number - square is greater than or equal to 0 and the number - square is not in visited
                1. Append (number - square, level + 1) to the queue
                2. Add number - square to visited
    4. Return -1 if no perfect square is found
    """
    def numSquares(self, n: int) -> int:
        queue = deque([(n, 0)]) # (number, level)
        visited = set()
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        while queue:
            num, level = queue.popleft()
            if num == 0:
                return level
            for square in squares:
                if num - square >= 0 and (num-square) not in visited:
                    queue.append((num-square, level+1))
                    visited.add(num-square)

