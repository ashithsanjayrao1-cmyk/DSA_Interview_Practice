class Meeting:
    def __init__(self,start,end,position):

        self.start = start
        self.end = end
        self.position = position

class Solution:
    def maxMeeting(self,start,end,n):
        meeting = []

        for i in range(n):
            meeting.append(Meeting(start[i],end[i],i+1))

        meeting.sort(key = lambda x: (x.end,x.position))

        ans = []

        count = 1

        free_time = meeting[0].end
        ans.append(meeting[0].position)

        for i in range(1,n):
            if meeting[i].start > free_time:

                count += 1
                free_time = meeting[i].end
                ans.append(meeting[i].position)


        return count


if __name__ == "__main__":
    # Test case: 6 meetings
    start = [0,3,1,5,5,8]
    end =   [5,4,2,9,7,9]
    n = 6
    
    s = Solution()
    max_count = s.maxMeeting(start, end, n)
    
    print(f"Maximum number of meetings: {max_count}")

        


 







