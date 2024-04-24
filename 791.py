class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lookup = defaultdict(int)

        for i, c in enumerate(order):
            lookup[c] = i

        return "".join(sorted(s, key=lambda x:lookup[x]))
    
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        res = []

        for c in order:
            if c in count:
                res.extend([c]*count[c])
                count.pop(c)
        
        for k, v in count.items():
            res.extend(k*v)

        return "".join(res)
