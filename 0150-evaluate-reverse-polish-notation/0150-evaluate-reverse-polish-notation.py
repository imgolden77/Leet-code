class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        valid = set('+-*/')
        for token in tokens:
            if token in valid:
                b= s.pop()
                a= s.pop()
                if token == "+":
                    s.append(a+b)
                if token == "-":
                    s.append(a-b)
                if token == "*":
                    s.append(a*b)
                if token == "/":
                    s.append(int(a/b))
            else:
                s.append(int(token))
            
        return s[0]
            