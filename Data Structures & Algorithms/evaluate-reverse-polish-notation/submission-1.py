import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    res = first + second
                elif token == "-":
                    res = first - second
                elif token == "*":
                    res = first * second
                else:
                    if second != 0:
                        res = math.trunc(first / second)
                    else:
                        res = 0
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()
