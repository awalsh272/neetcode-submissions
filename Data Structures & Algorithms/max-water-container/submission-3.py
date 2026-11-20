class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            max_area = max(max_area, area)

            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1

        return max_area
        