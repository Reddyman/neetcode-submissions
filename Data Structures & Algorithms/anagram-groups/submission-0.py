from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # set union
        # O(n*m) time
        # O(n*m) space
        anagram_dict = defaultdict(list)

        for string in strs:
            char_freq = [0] * 26

            for char in string:
                index_delta = ord(char) - ord("a")
                char_freq[index_delta] += 1
            # tuples can be dict keys due to immutability
            anagram_dict[tuple(char_freq)].append(string) 
        return list(anagram_dict.values())
