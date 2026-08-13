class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxarea = 0
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                width = i - 1 - (stack[-1]) if stack else i 
                maxarea = max(maxarea, height*width) 
            stack.append(i)
        return maxarea