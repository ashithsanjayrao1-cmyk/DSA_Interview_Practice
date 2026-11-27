class Solution():
    def NonOverlapping(self,intervals):

        if not intervals:
            return 0

        n = len(intervals)

        intervals.sort(key = lambda x: x[1])

        count = 1

        lastEndTime = intervals[0][1]

        for i in range(1,n):

            if intervals[i][0] >= lastEndTime:
                count += 1

                lastEndTime = intervals[i][1]


        return n-count
if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    s = Solution()
    print(f"Minimum intervals to remove: {s.NonOverlapping(intervals)}")