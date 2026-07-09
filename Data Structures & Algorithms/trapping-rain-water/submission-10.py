class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total_max = 0
        current_i = 0
        max_height = 0
        while l < r:
            fill = max(max_height - height[current_i], 0)
            max_height = max(max_height, min(height[l], height[r]))
            total_max += fill
            if height[l] < height[r]:
                l += 1
                current_i = l
            else:
                r -= 1
                current_i = r

        return total_max
        