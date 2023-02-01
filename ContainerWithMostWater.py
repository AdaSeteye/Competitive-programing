class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0
        while(i < j):
            depth = min(height[i], height[j])
            width = j - i
            if max_area < depth * width:
                max_area = depth * width
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_area
