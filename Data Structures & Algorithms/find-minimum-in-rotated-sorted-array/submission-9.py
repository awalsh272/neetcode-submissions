class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        min_num = nums[l]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] < nums[r]:
                return min(min_num, nums[l])
            
            min_num = min(min_num, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else: 
                r = mid - 1

        return min_num


        