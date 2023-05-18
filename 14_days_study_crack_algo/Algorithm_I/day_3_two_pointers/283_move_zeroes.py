class Solution:
    """
    1. Initialize a pointer called 'insert_pos'
    2. Iterate through each element 'num' in the list 'nums'
    3. For each 'num', check if it is not zero ('num != 0')
        a) if non-zero: move it to position indicated by insert_pos, and += 1
        b) if zero: skip and move to next element
    4. After iterating through 'nums' every non-zero element should be at the start.
        insert_pos will point to first index that is to be zero.
    5. Iterate from 'insert_pos' to the end and fill remaining with zero.
    6. List should now contain all the non-zero elements in the beginning in their original order
        and all the zeros are added at the end.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        # Initialize a pointer to keep track of the position to insert non-zero elements
        insert_pos = 0

        # Iterate through the list and move non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill the remaining positions with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0




