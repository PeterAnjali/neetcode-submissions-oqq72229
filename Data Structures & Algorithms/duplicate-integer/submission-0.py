class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for a in nums:
            a= nums.pop()
            if a in nums:
                return True
        return False
                   