class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # O(log(n)) time
        # O(k) space
        if nums is None or len(nums) == 0:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            midpoint = (high + low) // 2
            if (target == nums[midpoint]):
                return midpoint
            elif (target > nums[midpoint]):
                low = midpoint + 1
            else:
                high = midpoint - 1
        return -1
