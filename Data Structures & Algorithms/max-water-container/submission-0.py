class Solution:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            max_water = max(max_water, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water