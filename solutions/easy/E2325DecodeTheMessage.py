from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = ascii_lowercase

        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1

        for char in message:
            res += mapping[char]

        return res
