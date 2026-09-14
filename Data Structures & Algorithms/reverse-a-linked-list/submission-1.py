# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterate forwards on list
        # build new list in reverse
        # O(n) time
        # O(n) space
        curr_node = ListNode()
        while head is not None:
            curr_node.val = head.val
            next_node = ListNode()
            next_node.next = curr_node
            curr_node = next_node
            head = head.next
        return curr_node.next
