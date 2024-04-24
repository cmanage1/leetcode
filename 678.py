class Solution:
    def checkValidString(self, s: str) -> bool:
        # * can be treated as left, right or empty string
        # Can use stack again

        starCount = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append("(")
            elif c == "*":
                starCount += 1
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                elif starCount > 1:
                    starCount -= 1
                    if stack:
                        stack.pop()

        return stack == []
