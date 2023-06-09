# Concept
Day 1 of 14 days to crack the algorithm is all about utilizing *binary search* to get O(log n) solve time. All of these problems are easily solvable in O(n), but the task lies in creating algorithms to create O(log n) solve times, this is done through  *binary search*

## Binary search
Binary seach is simply said with words finding the middle of your list/values, then checking if your target is more or less, then adjusting either the left/low (if target > mid) or the right/high (if target < mid). We could of course use a for loop and iterate through every element, but this takes time the larger our list becomes.

### Example 1:
You have a *list* of the following values: [1, 2, 4, 5, 8, 9, 11], target is *9* <br>
left is the left-most index, *left* = 0 <br>
right is the right-most index, *right* = len(list) - 1 <br>
middle is the index in the middle of our list, *middle* = (*left* + *right*) // 2 <br>
middle in this case would give us the value 5, which is less than our *target* of 9, therefore we adjust our values: <br>
left is now the index middle was + 1, *left* = mid + 1. Visually this would make our list look like this after one iteration: <br>
~~[1, 2, 3, 4, 5,~~ *8*, 9, *11*] <br>
new middle value is between new left and right, *middle* = (*right* + *left*) // 2 <br>
middle is now **9** which is our target. <br>