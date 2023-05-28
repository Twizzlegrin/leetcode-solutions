class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':  # Skip all trailing spaces
            i -= 1
        while i >= 0 and s[i] != ' ':  # Count the length of the last word
            length += 1
            i -= 1
        return length
