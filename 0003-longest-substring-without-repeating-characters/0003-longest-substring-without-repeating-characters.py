class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length =[]
        order = []
        if s =="":
            return 0
        for i, l in enumerate(s):
            if i == len(s)-1:
                if l not in order:
                    order.append(l)
                    max_length.append(len(order)) 
                else:
                    max_length.append(len(order)) 
            elif l not in order:
                order.append(l)
            else:
                max_length.append(len(order))
                n=order.index(l)
                for j in range(n, -1, -1):
                    order.pop(j)
                order.append(l)
                
        
        return max(max_length)
            