class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take first string
        # traverse with each word and each char
        # O(n * m * c) time
        # O(c) space
        if strs is None or len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        current_index = 0
        start_over = True
        while (start_over):
            for i in range(1, len(strs)):
                if (current_index > len(strs[0]) - 1 or
                    current_index > len(strs[i]) - 1):
                    current_index -= 1
                    start_over = False
                    break
                elif strs[0][current_index] != strs[i][current_index]:
                    current_index -= 1
                    start_over = False
                    break
            current_index += 1
        return strs[0][0:current_index]

