class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixes = [0] * n
        suffixes = [0] * n

        prefix_max = height[0]
        suffix_max = height[-1]

        prefixes[0] = height[0]
        suffixes[-1] = height[-1]

        for i in range(1, n):
            prefixes[i] = max(height[i], prefixes[i-1])

        for i in range(n-2, -1, -1):
            suffixes[i] = max(height[i], suffixes[i+1])
        
        total_water = 0
        for i in range(len(height)-1):
            water = min(prefixes[i], suffixes[i])
            total_water += water - height[i]
        return total_water

        