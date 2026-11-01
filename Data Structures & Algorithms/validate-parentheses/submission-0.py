class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {'}': '{', ']': '[', ')': '('}
        for p in s:
            if p in paren_map:
                if not stack or stack[-1] != paren_map[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        if stack:
            return False
        return True
                