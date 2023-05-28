class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = str2 = ''
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        int1 = int(str1[::-1])
        int2 = int(str2[::-1])
        result = int1 + int2

        str3 = str(result)[::-1]


        head = l3 = ListNode(str3[0])
        for i in range(1, len(str3)):
            temp = ListNode(str3[i])
            l3.next = temp
            l3 = temp
        return head
