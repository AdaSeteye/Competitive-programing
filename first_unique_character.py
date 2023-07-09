class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = []
        counter = collections.Counter(s)
        for i in counter.keys():
            if counter[i] == 1:
                queue.append(i)
        for i in range(len(s)):
            if queue and s[i] == queue[0]:
                return i
        return -1
