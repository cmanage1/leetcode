class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # we can do this by making the number negative where it appears
        res = []
        
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n-1] < 0:
                res.append(n)
            nums[n-1] *= -1

        return res 
