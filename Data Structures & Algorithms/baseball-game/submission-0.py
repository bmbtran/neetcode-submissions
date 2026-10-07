class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for entry in operations:
            if entry == "+":
                scores.append(scores[-1] + scores[-2])
            elif entry == "D":
                scores.append(scores[-1] * 2)
            elif entry == "C":
                scores.pop()
            else:
                scores.append(int(entry))
        return sum(scores)
        