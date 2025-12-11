class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {')':'(', '}':'{', ']':'['}
        
        for i in s:
            if i in par_map.values():
                stack.append(i)
            elif i in par_map:
                if not stack or stack[-1] !=par_map[i]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
                
          