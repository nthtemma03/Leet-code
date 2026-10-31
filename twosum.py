class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = {}

        for i in range(len(nums)):
            ans_num = target - nums[i]

            if nums[i] in ans:
                return [i, ans[nums[i]]]
            ans[ans_num] = i 
            
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
                else:
                    continue
