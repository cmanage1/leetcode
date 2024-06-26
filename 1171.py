# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # delete consecutive sequences of nodes that sum to 0
        # slow and fast pointers?
        dummy = ListNode()
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {}

        curr = dummy

        while curr:
            prefix_sum += curr.val
            prefix_sum_map[prefix_sum] = curr
            curr = curr.next

        curr = dummy
        prefix_sum = 0
        
        while curr:
            prefix_sum += curr.val
            if prefix_sum in prefix_sum_map:
                curr.next = prefix_sum_map[prefix_sum].next
            curr = curr.next

        return dummy.next
