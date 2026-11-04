#Given: an array nums[...]

#1st approach
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans =0
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                nums[i]*= nums[i]
                ans += nums[i]
            else:
                continue
        return ans
#T(n)=)(n) with 2ms 

#2nd approach
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                ans+= nums[i]**2
            else:
                continue
        return ans
# 1ms
