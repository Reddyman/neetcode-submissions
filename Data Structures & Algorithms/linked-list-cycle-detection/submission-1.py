# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortoise and hare
        # two pointers iterate
        # if the pointers ever meet before getting to null
        # then it is proof there is a cycle
        # O(n) time
        # O(k) space
        slow, fast = head, head

        count = 0
        while slow is not None and fast is not None:
            if count % 2 == 1:
                slow = slow.next
            fast = fast.next
            if (slow == fast):
                return True
            count += 1

        return False