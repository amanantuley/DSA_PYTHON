class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odd = []

        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odd.append(i)

        return evens + odd
