class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        r = 0
        def minDist(heater, h):
            lo, hi = 0, len(heater) - 1
            dist = float('inf')
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                dist = min(dist, abs(heater[mid] - h))
                if heater[mid] < h:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return dist
        for house in houses:
            r = max(r, minDist(heaters, house))
        return r
            
