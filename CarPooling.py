class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        for i in range(len(trips)):
            arr[trips[i][1]] += trips[i][0]
            arr[trips[i][2]] -= trips[i][0]
        temp = 0
        for j in arr:
            temp += j
            if temp > capacity:
                return False
        return True
