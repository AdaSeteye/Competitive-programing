class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        max_val = head.val
        rest = self.removeNodes(head.next)
    
        if rest and rest.val > max_val:
            return rest
        else:
            head.next = rest
            return head
