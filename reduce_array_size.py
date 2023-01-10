class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        values = sorted(count.values(), reverse = True)
        n = len(arr)
        sign = n//2
        num_elts = 0
        for i in values:
            sign-=i
            num_elts+=1
            if sign <= 0:
                return num_elts
        return num_elts
