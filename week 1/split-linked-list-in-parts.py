# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1
        
        mainLen = length // k
        rem = length % k

        cur = head
        res = []

        for i in range(k):
            res.append(cur)

            for j in range(mainLen - 1 + (1 if rem else 0)):
                if not cur: break
                cur = cur.next
            rem -= (1 if rem else 0)
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
                
        return res
