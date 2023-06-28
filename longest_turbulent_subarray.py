class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i, j = 0, 1
        prevSign = ""
        max_len = 1
        while j < len(arr):
            if arr[j] < arr[j - 1] and prevSign != ">":
                max_len = max(max_len, j - i + 1)
                j += 1
                prevSign = ">"
            elif arr[j] > arr[j - 1] and prevSign !="<":
                max_len = max(max_len, j - i + 1)
                j += 1
                prevSign = "<"
            else:
                if arr[j] == arr[j - 1]:
                    j += 1
                prevSign = ""
                i = j - 1
        return max_len
