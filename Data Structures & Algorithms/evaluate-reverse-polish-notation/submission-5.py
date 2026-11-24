class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result_stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                result_stack.append(int(token))
            else:
                second = int(result_stack.pop())
                first = int(result_stack.pop())
                if token == "+":
                    res = first + second
                elif token == "-":
                    res = first - second
                elif token == "*":
                    res = first * second
                elif token == "/":
                    res = int(first/second)

                result_stack.append(res)

        return result_stack[0]
                



        