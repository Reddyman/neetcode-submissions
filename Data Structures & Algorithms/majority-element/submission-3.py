class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashset counter for each num
        # O(n) time
        # O(n) space
        if len(nums) == 1: return nums[0]

        nums_count_dict = {}
        for num in nums:
            if num in nums_count_dict:
                nums_count_dict[num] += 1
                if (nums_count_dict[num] > (len(nums) // 2)):
                    return num
            else:
                nums_count_dict[num] = 1
        return 0