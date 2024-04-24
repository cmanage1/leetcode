class Solution:
    # dp O(1) space
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        one, two, three = 0, 1, 1
        
        for i in range(3, n+1):
            tmp = three # save this for later
            three = one + two + three
            two = tmp
            one = two
        return three

    # dp array
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        seen = [0] * (n+1)
        seen[0] = 0
        seen[1] = 1
        seen[2] = 1

        for i in range(3, n):
            seen[i] = seen[i-3] + seen[i-2] + seen[i-1]
            
        return seen[-1] 

    # no dp, recursive
    def tribonacci(self, n: int) -> int:
        # trib 
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1) 
