class Solution:
    def iterative_binary_search(self, nums: list[int], target) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            mid_num = nums[mid]

            if mid_num > target:
                r = mid - 1
            elif mid_num < target:
                l = mid + 1
            else:
                return mid

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False

        row_l = 0
        row_r = len(matrix) - 1 

        while row_l <= row_r:
            row_mid = row_l + (row_r - row_l) // 2
            selected_row = matrix[row_mid]
            if target < selected_row[0]:
                row_r = row_mid - 1
            elif target > selected_row[-1]:
                row_l = row_mid + 1
            else:
                break

        if not row_l <= row_r:
            return False
        row_num = (row_r + row_l) // 2

        search = self.iterative_binary_search(matrix[row_num], target)
        if search == -1:
            return False
        else:
            return True
                

        