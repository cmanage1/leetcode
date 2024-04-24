class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElem = max(nums)
        l = r = 0
        count = res = 0

        while r < len(nums):
            if nums[r] == maxElem:
                count += 1

            while count >= k:
                if nums[l] == maxElem:
                    count -= 1
                res += len(nums)-r
                l += 1
            r +=1

        return res
