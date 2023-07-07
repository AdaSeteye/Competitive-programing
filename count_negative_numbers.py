class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        r = len(grid)
        c = len(grid[0])
        def search(r):
            l, h = 0, c - 1
            i = c
            while l <= h:
                mid = l + (h - l)//2
                if r[mid] < 0:
                    i = mid
                    h = mid - 1
                else:
                    l = mid + 1
            return i
        for j in range(r):
            ans += c - search(grid[j])
        return ans
