class Solution():
    def canWePlace(self,stalls,dist,k):

        cows_placed = 1
        last_placed = stalls[0]

        for i in range(1,len(stalls)):
            if stalls[i] - last_placed >= dist:
                cows_placed += 1
                last_placed = stalls[i]

            if cows_placed >= k:
                return True
        return False

    def aggressiveCow(self,stalls,k):

        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]

        ans = -1

        while low<= high:
            mid = (low+high)//2

            if self.canWePlace(stalls,mid,k):
                ans = mid
                low = mid+1

            else:
                high = mid-1

        return ans
    
s1 = Solution()
stalls = [0, 3, 4, 7, 10, 9]
k = 4  

print(s1.aggressiveCow(stalls,k))