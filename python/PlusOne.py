 #input[1, 2, 3]
#output [ 1,2, 4]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig_len = len(digits)
        for i in reversed(range(dig_len)):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits