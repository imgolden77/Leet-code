class Solution:
    def clearDigits(self, s: str) -> str:
        s_list=list(s)
        while sum([char.isdigit() for char in s_list])!=0:
            for i in range(len(s_list)):
                if s_list[i].isdigit() == True:
                    del s_list[i]
                    if i>0:
                        del s_list[i-1]
                    break
            else:
                continue
        return ''.join(s_list)
            