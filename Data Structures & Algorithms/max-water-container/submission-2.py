class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_area = max(max_area, area)

            l_diff = heights[l+1] - heights[l]
            r_diff = heights[r-1] - heights[r]
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            # else:
            #     break
        
        return max_area
        