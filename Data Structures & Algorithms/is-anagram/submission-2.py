class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort each string O(nlog(n)) then compare
        return sorted(s) == sorted(t)