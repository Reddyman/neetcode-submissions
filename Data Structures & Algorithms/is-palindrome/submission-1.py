class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, iterate from low, high
        # O(n) time
        # O(k) space
        low, high = 0, len(s) - 1

        while (low < high):
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            if not s[low].lower() == s[high].lower():
                return False
            low += 1
            high -= 1
        return True