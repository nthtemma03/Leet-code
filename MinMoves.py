#1st approach
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        inc = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[j]+=1
                    inc +=1
                elif nums[i]<nums[j]:
                    nums[i]+=1
                    inc +=1
                else:
                    continue
        return inc

# this only solves elements that are +1 or -1 apart

#2nd approach
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        inc = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                while nums[i] != nums[j]:
                    if nums[i]>nums[j]:
                        nums[j]+=1
                        inc +=1
                    else:
                        nums[i]+=1
                        inc +=1
        return inc
# this approach passes with long execution time of n^2

#3rd approach
#using max() to find to largest instead of looping through 2 for loops
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        inc = 0
        largest = max(nums)

        for i in range(len(nums)):
            if nums[i] < largest:
                inc += largest - nums[i]
            else:
                continue
        return inc

#4th approach
#using (n*largest) - sum(nums). This approach finds the maximum steps to make every element == to the largest. Then find the sum of the array to know the different.
#The difference is the number of steps needed
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        largest = max(nums)
        inc = (len(nums)*largest)-(sum(nums))
        return inc

#5th approach. Most optimal from Leetcode
#This finds the largest number in the array and use the for loop to find the difference at every element, then update it to the answer
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans=0
        a=max(nums)
        for i  in nums:
            ans+=(a-i)
        return ans
        
