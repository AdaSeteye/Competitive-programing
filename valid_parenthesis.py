class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif stack and s[i] == ")" and stack[-1] == "(" or stack and s[i] == "]" and stack[-1] == "[" or stack and s[i] == "}" and stack[-1] == "{":
                    stack.pop()
            else:
                stack.append(s[i])
        return False if stack else True
