class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate in reverse order
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + carry
            
            digits[i] = tmp % 10
            carry = tmp // 10

        if carry:
            digits.insert(0, carry)

        return digits
