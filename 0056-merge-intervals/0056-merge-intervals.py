class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=1
        res=[]
        n= len(intervals)
        intervals.sort()
        new=intervals[0]
        print("debug0:", intervals)
        if n==1:
            return intervals

        while i<n and intervals[i][1]<new[0]:
            res.append(intervals[i])
            print("debug1:",i, res)
            i +=1
            
        while i<n:
            if intervals[i][0]<=new[1]:
                new[0]=min(new[0], intervals[i][0])
                new[1]=max(new[1], intervals[i][1])
                  
            else:
                res.append(new)
                new = intervals[i]
            i+=1  
        
        res.append(new)
        print("debug3:", i, res)
            
        return res
        
