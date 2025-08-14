class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=1
        res=[]
        intervals.sort()
        n= len(intervals)
        new=intervals[0]
        if n==1:
            return intervals
            
        while i<n:
            if intervals[i][0]<=new[1]:
                new[0]=min(new[0], intervals[i][0])
                new[1]=max(new[1], intervals[i][1])
                  
            else:
                res.append(new)
                new = intervals[i]
            i+=1  
        
        res.append(new)
            
        return res
        
