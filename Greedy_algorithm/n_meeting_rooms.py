class Solution:
    
    def maximumMeetings(self,n,start,end):
        # code here
        sorted_arrays = sorted(zip(end, start), key=lambda x: x[0])
        sorted_end, sorted_start = zip(*sorted_arrays)
        max_meeting=0
        endtime=-1
        for i in range(n):
            if sorted_start[i]>endtime:
                max_meeting+=1
                endtime=sorted_end[i]
        return max_meeting
                