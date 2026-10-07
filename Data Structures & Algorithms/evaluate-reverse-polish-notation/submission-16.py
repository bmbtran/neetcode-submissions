class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #there can be more than 2 before an operator
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(first / second)
        return int(stack[0])