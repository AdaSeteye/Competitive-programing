class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        else:
            l = r = addL = head
            while r and r.next:
                addL = l
                l = l.next
                r = r.next.next
            addL.next = addL.next.next
            return head
