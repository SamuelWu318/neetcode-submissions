class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total_max = 0
        max_height = 0
        while l < r:
            max_height = max(max_height, min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
                total_max += max(max_height - height[l], 0)
            else:
                r -= 1
                total_max += max(max_height - height[r], 0)

        return total_max
        