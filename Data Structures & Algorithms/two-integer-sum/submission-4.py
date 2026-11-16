class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            # j starts at 0 but its the 1st index, so add 1
            for j, num2 in enumerate(nums[i+1:]):
                summed = num1 + num2
                if summed == target:
                    return [i, i+j+1]

        