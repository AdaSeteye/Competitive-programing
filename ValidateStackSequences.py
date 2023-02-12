class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return not stack
