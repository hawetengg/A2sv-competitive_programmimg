# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        cur = head

        while cur.next is not None:
            cur = cur.next
            count += 1

        if count == n:
            head = head.next
            return head
        k = count - n
        prev = None
        cur = head

        while k > 0:
            prev = cur
            cur = cur.next
            k -= 1
        prev.next = cur.next
        return head
        