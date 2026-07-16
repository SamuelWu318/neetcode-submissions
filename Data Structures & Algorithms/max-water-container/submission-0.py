class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            best = max(best, water)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return best