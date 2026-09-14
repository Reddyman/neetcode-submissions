class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # mutate nums list
        # O(n) time
        # O(k) space
        write_index = 0
        read_index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                read_index += 1
            else:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index