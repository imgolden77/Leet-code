class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for token in tokens:
            try:
                int(token)
                s.append(int(token))
                # print("debug_digit:", s)
            except ValueError: 
                if token == "+":
                    b= s.pop()
                    a= s.pop()
                    s.append(a+b)
                    # print("debug+:", s)
                elif token == "-":
                    b= s.pop()
                    a= s.pop()
                    s.append(a-b)
                    # print("debug-:", s)
                elif token == "*":
                    b= s.pop()
                    a= s.pop()
                    s.append(a*b)
                    # print("debug*:", s)
                elif token == "/":
                    b= s.pop()
                    a= s.pop()
                    s.append(int(a/b))
                    # print("debug/:", s) 
        return s[0]
            