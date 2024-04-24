class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones, zeroes = 0, 0

        for n in s:
            if n == "0":
                zeroes += 1
            if n == "1":
                ones += 1

        res = ""
        ones -=1 # we will add this later

        for _ in range(ones):
            res += "1"
        for _ in range(zeroes):
            res += "0"

        return res + "1"
