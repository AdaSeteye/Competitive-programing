class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            odd = head
            even = evenHead = head.next
            while odd.next and even.next:
                tempOdd = odd.next.next
                tempEven = even.next.next
                odd.next = tempOdd
                temp = odd
                odd = tempOdd
                even.next = tempEven
                even = tempEven

        if not odd:
            temp.next = evenHead
        else:
            odd.next = evenHead
        return head
