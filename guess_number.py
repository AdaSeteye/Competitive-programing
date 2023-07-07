class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            mid = l + (h - l)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                h = mid - 1
            else:
                l = mid + 1
