class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        triples = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 2):
            l = i + 1
            r = len(sorted_nums) - 1
            sum_to = target - sorted_nums[i]
            while l < r:
                three_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                
                
                if three_sum < target:
                    l += 1
                elif three_sum > target:
                    r -= 1

                elif three_sum == target:
                    triple = [sorted_nums[i], sorted_nums[l], sorted_nums[r]]
                    if triple not in triples:
                        triples.append(triple)
                    l += 1
                    r -= 1

        return triples
