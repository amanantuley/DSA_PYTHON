class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = digits[::-1]
        one = 1
        i = 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] =0
                else:
                    digits[i] = digits[i] + 1
                    one = 0
            else:
                digits.append(1)
                one = 0     
            i = i + 1
        return digits[::-1]
