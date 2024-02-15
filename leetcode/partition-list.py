# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        stack = []
        prev = None
        tmp = head

        while tmp:
            if tmp.val < x and not prev:
                min_Node = tmp
                tmp = tmp.next
                head = tmp
                min_Node.next = None
                stack.append(min_Node)
            elif tmp.val < x:
                min_Node = tmp
                prev.next = tmp.next
                tmp = tmp.next
                min_Node.next = None
                stack.append(min_Node)
            else:
                prev = tmp
                tmp = tmp.next
        while stack:
            node = stack.pop()
            node.next = head
            head = node
        return head

        