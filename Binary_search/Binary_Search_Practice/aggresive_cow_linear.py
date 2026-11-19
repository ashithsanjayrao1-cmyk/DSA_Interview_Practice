class Solution():
    def func(self,arr,dist,cow):

        count_cow = 1
        n = len(arr)

        last_placed = arr[0]

        for i in range(n):

            if arr[i] - last_placed > dist:
                count_cow += 1
                last_placed = arr[i]

            if count_cow >= cow:
                return True
            return False
    def agressiveCow(self,arr,k):
        arr.sort()

        max_dist = arr[-1] - arr[0]

        for i in range(1,max_dist+1):
            if self.func(arr,i,k) == False:
                return i-1

        return max_dist
s1 = Solution()
print(s1.agressiveCow([0,3,4,7,9,10],4))
