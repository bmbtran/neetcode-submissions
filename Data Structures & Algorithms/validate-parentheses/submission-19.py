class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"(": ")", "[": "]", "{" : "}"}
        stack = []
        for c in s:
            if c in openToClose.values():
                if not stack or openToClose[stack[-1]] != c:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack

