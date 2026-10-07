class Solution:
    def operator(self, first, operator, second):
        if operator == "+":
            return first + second
        if operator == "-":
            return second - first
        if operator == "*":
            return first * second
        if operator == "/":
            return int(second / first)
        
    def evalRPN(self, tokens: List[str]) -> int:
        #res = 1,
        #while L < len(tokens) and R < len(tokens) pointer, L = 2, R = +
        # res = res R L
        # L, R +=2
        #wrong bcs wrong assumptions

        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                first = stack.pop()
                second = stack.pop()
                res = self.operator(first, tokens[i], second)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
