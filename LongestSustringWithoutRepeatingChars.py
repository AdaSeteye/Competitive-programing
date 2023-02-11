class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        maxLength = -1
        if (len(s) == 0):
            return 0
        elif(len(s) == 1):
            return 1
        for i in list(s):
            current = ''.join(i)
            if (current in temp):
                temp = temp[temp.index(current) + 1:]
            temp = temp + ''.join(i)
            maxLength = max(len(temp), maxLength)
        return maxLength
