class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            curr = self.countOnes(i)
            ans.append(curr)
        return ans

    def countOnes(self, i):
        res = 0
        while i > 0:
            res += i & 1 # this checks if the last digit is 1
            i >>= 1
        return res
