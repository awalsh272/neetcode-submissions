class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        min_num = nums[l]
        pivot_ind = l
        if len(nums) > 1:
            while l <= r:
                mid = l + (r - l) // 2
                if nums[l] < nums[r]:
                    if nums[l] < min_num:
                        min_num = nums[l]
                        pivot_ind = l
                    break
                
                if nums[mid] < min_num:
                    min_num = nums[mid]
                    pivot_ind = mid
                
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else: 
                    r = mid - 1

        def binary_search(nums: list[int], target: int, l: int, r: int) -> int:
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1

                else:
                    return mid

            return -1

        #print(pivot_ind, nums[:pivot_ind], nums[pivot_ind:])
        s = binary_search(nums, target, 0, pivot_ind)
        if s != -1:
            return s
        else:
            return binary_search(nums, target, pivot_ind, len(nums)-1)



        