class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : "{"
        }
        stack = []
        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != closeToOpen[c]:
                    return False

        return True if len(stack) ==0 else False
        #[
        #]

        #wrong cases:
        #if close w wrong respective bracket
        #or close without any opening

    
