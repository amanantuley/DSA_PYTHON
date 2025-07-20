class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            squared = nums[i] ** 2
            result.append(squared)

        result.sort()
        return result        