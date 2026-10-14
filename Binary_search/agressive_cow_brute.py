class Solution():
    def canWePlace(self,stalls,dist,k):

        cows_placed = 1
        last_places_pos = stalls[0]

        for i in range(1,len(stalls)):

            if stalls[i] - last_places_pos >= dist:
                cows_placed += 1
                last_places_pos = stalls[i]


            if cows_placed >= k:
                return True

        return False

    def aggressiveCow(self,stalls,k):

        stalls.sort()

        max_dist = stalls[-1] - stalls[0]

        for dist in range(1,max_dist+1):

            if self.canWePlace(stalls,dist,k) == False:
                return dist-1

        return max_dist
    
s1 = Solution()
stalls = [0, 3, 4, 7, 10, 9]
k = 4

print(s1.aggressiveCow(stalls,k))

        