class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = { ")" : "(", "]" : "[", "}" : "{" }
        for par in s:
            if par in close_map:
                if stack and stack[-1] == close_map[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)

        return True if not stack else False

        