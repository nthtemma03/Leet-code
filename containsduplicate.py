class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for n in nums:
            if nums.count(n) > 1:
                return True
            else:
                return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for n in nums:
            if nums.count(n) > 1:
                return True
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        contain = []

        for n in nums:
            if n in contain:
                return True
            contain.append(n)
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        contain = {}

        for n in nums:
            if n in contain:
                return True
            contain[n] = True
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

        
