class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if target not in nums:
            return [-1 , -1]
            
        j = len(nums) - 1
        for i in range(len(nums)):
            for k in range(j , -1 , -1):
                if nums[i] == target and nums[k] == target:
                    return [i , k]

        return  [ -1 , - 1]            
        
       