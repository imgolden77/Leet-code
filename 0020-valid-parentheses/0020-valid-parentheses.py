class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stack=[]
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i ==")":
                if "(" not in stack:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i =="]":
                if "[" not in stack:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif i =="}":
                if "{" not in stack:
                    return False
                elif stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False