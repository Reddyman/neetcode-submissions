class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort implementation
        # O(nlog(n)) time
        # O(n) space
        n = len(nums)
        temp = [0] * n

        def merge_sort(left, right):
            # A range of 0 or 1 elements is sorted
            if left >= right:
                return
            
            # merge nums[left:middle] and nums[middle:right]
            middle = (left + right) // 2

            merge_sort(left, middle)
            merge_sort(middle + 1, right)

            i = left
            j = middle + 1
            k = left

            while i <= middle and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            
            # copy remaining elements from the left half
            while i <= middle:
                temp[k] = nums[i]
                i += 1
                k += 1
            
            # copy remaining elements from the right half
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
            
            # copy the merged range back into nums
            for k in range(left, right + 1):
                nums[k] = temp[k]
    
        merge_sort(0, len(nums) -1)
        return nums