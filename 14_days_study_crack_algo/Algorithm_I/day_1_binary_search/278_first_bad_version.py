# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while (l < r):
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

# First immediate solution is obvious O(n), next step is optimization:
#   def firstBadVersion(self, n: int) -> int:
#     for i in range (1, n+1):
#            if isBadVersion(i) == True:
#               return i