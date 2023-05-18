class Solution:
    """
    1. Initialize two pointers, l (left) and r (right). Pointing to first and last element.
    2. Use a whilel oop that continues until l < r
    3. We calculate l + r (curr_sum)
    4. If the current sum equals target, we directly return those indices '[l + 1, r + 1]'
    5. If the current sum is less than target, we move the left pointer one step to the right
    6. If the current sum is greated than targert, we move the right pointer one step to the left
    7. If loop finishes without finding a solution, we return an empty list.

    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # We initialize the two pointers
        l = 0
        r = len(numbers) - 1

        # Create the loop that iterates as long as left pointer is less than right pointer
        while l < r:

            # We need to save the value in a variable
            curr_sum = numbers[l] + numbers[r]


            # Check if the current sum is equal to target
            if curr_sum == target:
                return [l + 1, r + 1]  # Return the indices directly

            # If target is higher, move left pointer right. If lower, move right pointer left.
            if curr_sum < target:
                l += 1
            else:
                r -= 1

        return []  # Return an empty list if no solution is found
