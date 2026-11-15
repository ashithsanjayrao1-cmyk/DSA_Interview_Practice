class Solution():
    def func(self,bloomday,day,m,k):

        n = len(bloomday)



        count = 0
        bouquets = 0

        for i in range(n):

            if bloomday[i] <= day:

                count += 1

            else:

                bouquets += (count//k)
                count = 0

        bouquets += (count//k)

        if bouquets >= m:
            return True
        else:
            return False

    def bouquets(self,bloomday,m,k):

        n = len(bloomday)

        


        if m*k > n:
            return -1

        for i in range(min(bloomday),max(bloomday)+1):

            possible = self.func(bloomday,i,m,k)

            if possible == True:
                return i
s1 = Solution()
arr = [7,7,7,7,13,11,12,7]
print(s1.bouquets(arr,2,3))
        
        


            