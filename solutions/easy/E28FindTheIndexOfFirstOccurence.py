class Solution:
    """
    First solution is a brute force solution where we check if the needle is in the haystack. Second solution is a KMP
    solution where we build the lps array and use it to find the needle in the haystack. Third solution is a
    Boyer-Moore solution where we build the bad character table and use it to find the needle in the haystack. Fourth
    solution is a Rabin-Karp solution where we use a rolling hash to find the needle in the haystack
    """

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if needle in haystack:
            return haystack.index(needle)

        return -1

    #  KMP solution
    def build_lps(self, needle: str):
        lps = [0] * len(needle)
        j = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[j]:
                lps[i] = j + 1
                j += 1
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        lps = self.build_lps(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
            if j == len(needle):
                return i - j
        return -1

    # Boyer-Moore solution
    def build_bad_char_table(self, needle: str):
        bad_char_table = {}
        for i in range(len(needle)):
            bad_char_table[needle[i]] = i
        return bad_char_table

    def bm_strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        bad_char_table = self.build_bad_char_table(needle)
        i = 0
        while i < len(haystack) - len(needle) + 1:
            j = len(needle) - 1
            while j >= 0 and haystack[i + j] == needle[j]:
                j -= 1
            if j < 0:
                return i
            else:
                if haystack[i + j] in bad_char_table:
                    i += max(1, j - bad_char_table[haystack[i + j]])
                else:
                    i += j + 1
        return -1

    # Rabin-Karp solution
    def rabin_karp_strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def hash(s):
            h = 0
            for i in range(len(s)):
                h += ord(s[i]) * (26 ** (len(s) - i - 1))
            return h

        needle_hash = hash(needle)
        haystack_hash = hash(haystack[:len(needle)])
        if haystack_hash == needle_hash:
            return 0

        for i in range(1, len(haystack) - len(needle) + 1):
            haystack_hash -= ord(haystack[i - 1]) * (26 ** (len(needle) - 1))
            haystack_hash *= 26
            haystack_hash += ord(haystack[i + len(needle) - 1])
            if haystack_hash == needle_hash:
                return i
        return -1
