class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n), using this approach bucket sort
        # Max heap approach is O(klogn) so this is better

        count = {} # key=number, value=count
        freq = [[] for _ in range(len(nums)+1)] #key=count, value=number

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
