class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])

            if len(hashset) > k:
                hashset.remove(nums[i - k])
            
        return False