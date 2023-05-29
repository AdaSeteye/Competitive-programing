class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print("arr", arr)

        n = len(arr)
        maxSum = 2
        for i in range(n//2):
            newSum = arr[i] + arr[n - 1 - i]
            maxSum = max(maxSum, newSum)
        return maxSum
