class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        mid=[float('inf'), float('inf')]
        i=0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)

            if newInterval[0] in range(interval[0], interval[1]+1):
                mid[0]=interval[0]
            if newInterval[1] in range(interval[0], interval[1]+1):
                mid[1]=interval[1]
            if interval[0] > newInterval[1]:
                res.append(interval)
        if mid[0]==float('inf'):
            mid[0]=newInterval[0]
        if mid[1]==float('inf'):
            mid[1]=newInterval[1]
        
        res.append(mid)
        res.sort()
        return res





