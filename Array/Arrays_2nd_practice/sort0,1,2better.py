class Solution():

    def sortbetter(self,arr):
        n = len(arr)
        count0 = 0
        count1 = 0
        count2 = 0


        for i in arr:
            if i == 0:
                count0 += 1
            elif i == 1:
                count1 +=1
            else:
                count2 +=1

        for i in range(count0):
            arr[i] = 0

        for i in range(count0,count0+count1):
            arr[i] = 1

        for i in range(count0 + count1,n):
            arr[i] = 2

        return arr

s1 = Solution()

print(s1.sortbetter([2,1,0,2,0,1,1,2,0,0,0,1,2]))