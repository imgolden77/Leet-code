class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        r=0
        for token in tokens:
            try:
                int(token)
                s.append(int(token))
                # print("debug_digit:", s)
            except ValueError: 
                if token == "+":
                    b= s.pop()
                    a= s.pop()
                    r=a+b
                    s.append(r)
                    # print("debug+:", s)
                elif token == "-":
                    b= s.pop()
                    a= s.pop()
                    r=a-b
                    s.append(r)
                    # print("debug-:", s)
                elif token == "*":
                    b= s.pop()
                    a= s.pop()
                    r=a*b
                    s.append(r)
                    # print("debug*:", s)
                elif token == "/":
                    b= s.pop()
                    a= s.pop()
                    r=a/b
                    s.append(int(r))
                    # print("debug/:", s) 
        return s[0]
            