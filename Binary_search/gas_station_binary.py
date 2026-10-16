class Solution():
    def counstStation(self,arr,target_dist):

        count = 0

        for i in range(len(arr)-1):
            gap = arr[i+1] - arr[i]

            stations_needed = int(gap/target_dist)

            if gap == (stations_needed * target_dist):
                stations_needed -= 1

            count += stations_needed

        return count

    def findSmallestMaxDist(self,stations,k):
        n = len(stations)

        low = 0.0

        high = 0.0

        for i in range(n-1):
            high = max(high,float(stations[i+1]-stations[i]))

        while high - low > 1e-6:
            mid = (low+high)/2.0

            if self.counstStation(stations,mid) <= k:
                high = mid

            else:

                low = mid

        return high

s1 = Solution()
stations = [1, 2, 3, 4, 5]
k = 4

s1.findSmallestMaxDist(stations,k)