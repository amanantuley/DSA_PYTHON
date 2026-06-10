class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # for n^2 we will use 2 pointer
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(len(nums)):
            left = i + 1
            right = n - 1
            while left < right :
                total =  nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i] , nums[left] , nums[right]])
                    left = left + 1
                    right = right - 1
                elif total < 0:
                    left = left + 1
                else:
                    right = right - 1


        return ans
                
            

