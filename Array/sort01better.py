class Solution():

    def sortcolors(self,arr):
        arr.sort()
        return arr
    def sortbetter(self,arr):

        n =len(arr)

        count0 = 0
        count1 = 0
        count2 = 0


        for num in arr:

            if num == 0:
                count0 += 1

            elif num == 1:
                count1 +=1

            else:
              
                count2 +=1


        for i in range(count0):
            arr[i] = 0

        for i in range(count0,count0 + count1):
            arr[i] = 1

        for i in range(count0+count1,n):
            arr[i] = 2

        return arr

s1 = Solution()
arr = [2,0,2,1,1,0]

print(s1.sortbetter(arr))

        