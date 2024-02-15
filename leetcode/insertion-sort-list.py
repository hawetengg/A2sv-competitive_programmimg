# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        arr.sort()
        res = ListNode()
        temp = res

        for i in range(len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return res.next
        