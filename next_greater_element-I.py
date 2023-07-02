class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        ans = defaultdict(lambda: -1)
        for i in nums2:
            while stack and stack[-1] < i:
                ans[stack[-1]] = i
                stack.pop()
            stack.append(i)
        for num in nums1:
            res.append(ans[num])
        return res
