from collections import Counter

"""
1. Initialize a counter object 'cntr' by counting occurrence of chars in 's1'
2. Set the window size 'w' to the length of 's1'
3. Iterate for each index in the range of 0 -> s2 - 1
4. Check if current character at index 'i' in 's2' exists in 'cntr'
    If: decrease count by 1
5. Check if current index 'i' is greater than or equal to the window size 'w'
     AND if the char at 'i-w' exists in the 'cntr' object.
        If: increase count by 1
6. Check if all values in 'cntr' are equal to 0
    If: Means current window in 's2' contains a permutation of s1
7. If loop completes without finding a permutation in any window of 's2', 
    it means no permutation of 's1' exists in 's2'. Return 'False' to indicate.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1

            if i >= w and s2[i - w] in cntr:
                cntr[s2[i - w]] += 1

            if all([cntr[i] == 0 for i in cntr]):
                return True

        return False
