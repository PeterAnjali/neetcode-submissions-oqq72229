class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count>1:
            return[0]*len(nums)        
        total_prod = math.prod(x for x in nums if x!=0)
        result=[]
        for i,x in enumerate(nums):
            if zero_count ==1:
                result.append(total_prod if x ==0 else 0)
            else:
                result.append(total_prod//x)
        return result