class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = []

        for s in tokens:
            if s == "+":
                n1, n2 = curr.pop(), curr.pop()
                curr.append(n2+n1)
            elif s == "-":
                n1, n2 = curr.pop(), curr.pop()
                curr.append(n2-n1)
            elif s == "*":
                n1, n2 = curr.pop(), curr.pop()
                curr.append(n2*n1)
            elif s == "/":
                n1, n2 = curr.pop(), curr.pop()
                curr.append(int(n2/n1))
            else:
                curr.append(int(s))
        
        return curr[0]
