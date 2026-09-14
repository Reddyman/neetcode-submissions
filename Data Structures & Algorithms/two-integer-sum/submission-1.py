class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate over each num, store in hashmap
        # calculate delta between target and each num
        # perform a lookup in hashamp to check a match
        # O(n) time
        # O(n) space
        num_dict = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in num_dict:
                return [num_dict[delta], i]
            num_dict[nums[i]] = i
        return []