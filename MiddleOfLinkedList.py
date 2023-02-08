class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        temp1 = temp2 = head
        while temp1:
            temp1 = temp1.next
            size+=1
        middle = size//2

        count = 0
        while temp2:
            if count == middle:
                return temp2
            else:
                temp2 = temp2.next
                count+=1
        return None
