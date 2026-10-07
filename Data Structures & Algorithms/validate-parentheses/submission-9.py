class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []
        if len(s) <= 1:
            return False
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if hashMap[c] != stack.pop():
                    return False
                
        return not stack
