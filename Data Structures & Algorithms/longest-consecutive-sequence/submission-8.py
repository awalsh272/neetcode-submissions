class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        longest_streak = 1
        streak_len = 1

        for i in range(1, len(sorted_nums)):

            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            if sorted_nums[i] - sorted_nums[i-1] == 1:
                streak_len += 1
            else:
                streak_len = 1
            
            longest_streak = max(longest_streak, streak_len)
            
        return longest_streak
        