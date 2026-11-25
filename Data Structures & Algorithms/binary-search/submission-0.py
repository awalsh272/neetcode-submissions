class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            mid_num = nums[mid]
            if mid_num == target: 
                return mid
            elif mid_num > target:
                r = mid - 1
            elif mid_num < target:
                l = mid + 1

        return -1
        
         