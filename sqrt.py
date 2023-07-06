class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 1, x
        while l <= r:
            mid = l + (r - l)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
        return r
                
        
        
