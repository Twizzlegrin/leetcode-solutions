class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # x in range(len(nums)) so we can modify items in the array.
        for x in range(len(nums)):
            nums[x] *= nums[x]
        nums.sort()
        return nums

