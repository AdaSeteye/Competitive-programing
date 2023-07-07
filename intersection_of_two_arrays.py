class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        def binary_search(arr, target):
            arr.sort()
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        for i in nums1:
            if binary_search(nums2, i) and not i in ans:
                ans.append(i)
        return ans
