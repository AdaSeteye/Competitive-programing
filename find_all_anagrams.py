class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j = 0, len(p)
        output = []
        counter = collections.Counter(p)
        while j <= len(s):
            window = s[i:j]
            if collections.Counter(window) == counter:
                output.append(i)
            i += 1
            j += 1
        return output
