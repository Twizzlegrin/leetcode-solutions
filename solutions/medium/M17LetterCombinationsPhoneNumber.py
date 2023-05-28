from typing import List
import itertools


class Solution:
    """
    1. Create a number dictionary to translate the integers to corresponding characters
    2. Translate the string to a set of digits, 'digit_sets'
    3. Use itertools to find all possible combinations
    """
    def letterCombinations(self, digits: str) -> List[str]:
        number_dictionary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits:  # Edge case where if there are no digits we return an empty list
            return []

        digit_sets = [number_dictionary[digit] for digit in digits]
        combinations = [''.join(combination) for combination in itertools.product(*digit_sets)]

        return combinations