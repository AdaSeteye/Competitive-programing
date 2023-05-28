class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr1 = []
        arr2 = []
        prev = None
        curr = temp = temp2 = temp3 = head
        while temp2:
            arr1.append(temp2.val)
            temp2 = temp2.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        temp3 = prev
        while temp3:
            arr2.append(temp3.val)
            temp3 = temp3.next
        print("arr1", arr1)
        print("arr2", arr2)
        if arr1 == arr2:
            return True
        return False
