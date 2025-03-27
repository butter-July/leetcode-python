class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            if carry == 0:
                break
        if carry == 1:
            digits = [1] + digits
        return digits
