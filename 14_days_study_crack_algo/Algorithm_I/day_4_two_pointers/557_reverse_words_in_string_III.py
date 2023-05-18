class Solution:
    def reverseWords(self, s: str) -> str:
        """
        1. String is split into individul words using the .split() method, stored in words
        2. A list comprehension is used to create new list, reversed_words, where each word
            from words is reversed. This is done with slicing ('word[::-1]')
        3. The reversed words are joined together into a single string with the '.join()' method.
            The '' '' space character is used as the separator to add whitespace between reversed words
        4. The resulting reversed string is stored in the 'reversed_string' variable.
        5. We return reversed_string
        """

        #   Split the string into words
        words = s.split()

        #   Reverse each word in the list
        reversed_words = [word[::-1] for word in words]

        # Join the reversed words with whitespace
        reversed_string = ' '.join(reversed_words)

        return reversed_string