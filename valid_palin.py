class Solution:
    def isPalindrome(self, s: str) -> bool:
        concatenatedStr = ''
        for i in s:
            if i.isalnum():
                concatenatedStr += i.lower()

        if len(concatenatedStr) == 0:
            return True
        l, r = 0, len(concatenatedStr) - 1
        while(l <= r):
            if concatenatedStr[l] != concatenatedStr[r]:
                return False
            l += 1
            r -= 1
        return True
