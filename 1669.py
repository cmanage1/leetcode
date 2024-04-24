# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        curr.next = list1

        start, end = None, None

        i = 0
        while curr:
            if i == a:
                start = curr
            elif i == b:
                end = curr
            curr = curr.next
            i += 1

        end_l2 = list2
        while end_l2.next:
            end_l2 = end_l2.next

        end_l2.next = end
        start.next = list2
        return dummy.next
