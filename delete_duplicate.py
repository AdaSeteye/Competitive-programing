class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr:
            while ptr.next and ptr.next.val == ptr.val:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return head
