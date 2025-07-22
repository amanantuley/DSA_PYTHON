class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = list(heights)

        expected.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count = count + 1

        return count
        