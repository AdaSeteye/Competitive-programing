class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        stack = stack[:len(stack) - k]
        result = ''.join(stack)
        return str(int(result)) if result else '0'
