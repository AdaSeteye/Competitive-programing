class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        while current:
            if current.next and current.next.next and current.next.val == current.next.next.val:
                temp = current.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                current.next = temp.next
            else:
                current = current.next
        return dummy.next
