class Solution:
    def binarysearch(self, arr, k):
        start = 0
        end = len(arr) - 1
        result = -1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == k:
                result = mid
                end = mid - 1 
            elif arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1

        return result
