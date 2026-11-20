class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        print(nums)
        triples = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target_num = nums[i]

            if target_num > 0:
                break
            if i > 0 and target_num == nums[i-1]:
                continue
            
            while l < r:
                triple = [target_num, nums[l], nums[r]]
                summed = sum(triple)
                if summed == 0:
                    triples.append(triple)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif summed > 0:
                    r -= 1
                elif summed < 0:
                    l += 1

        return triples


            
        