class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. Initialize the variables 'seen', 'start', and 'longest_len'
        2. Iterate through the chars of the input string 's'
        3. Check if 'char' is already present in 'seen' dictionary
        4. Update the 'seen' dictionary with the most recent occurence of character: 'seen[char] = i'
        5. Calculate length of current substring: 'current_len = i - start + 1'
        6. Check if current length is greater than the length of longest ('current_len > longest_len)
            if: update longest_len
        7. After iterating through entire string, return longest_len
        """

        seen = {}  # Dictionary to hold chars
        start = 0  # Start index we use to determine when our current substring starts
        longest_len = 0  # Length of longest substring

        for i, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1

            seen[char] = i
            current_len = i - start + 1

            if current_len > longest_len:
                longest_len = current_len
        return longest_len
