class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: 
            return "0"
        l = (1 << n) - 1    
        if k == (l + 1) / 2:
            return "1"
        elif k < (l + 1) / 2:
            return self.findKthBit(n - 1, k)
        else:
            return str(1 - int(self.findKthBit(n - 1, l - k + 1)))
