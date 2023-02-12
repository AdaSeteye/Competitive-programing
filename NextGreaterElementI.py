class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index1 = {n:i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            temp = nums2[i]
            while stack and temp > stack[-1]:
                val = stack.pop()
                index = index1[val]
                result[index] = temp
            if temp in index1:
                stack.append(temp)
        return result
