class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if (n % 2 == 0):  # if n%2 == 0, it means n is already a multiple of 2.
            return n
        else:
            return 2 * n  # otherwise we would multiply n with 2 to find the smallest positive integer
