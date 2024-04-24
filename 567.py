class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 must be smaller than s2 for it to be a permutation of s2
        if len(s1) > len(s2):
            return False

        # Count
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1
 
        # Calculate sliding window
        for i in range(len(s2) - len(s1)):
            if s1_count == s2_count:
                return True

            # reduce leaving char count into window
            s2_count[ord(s2[i]) - ord('a')] -= 1

            # increate introduced char count into window
            s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1

        return s1_count == s2_count
