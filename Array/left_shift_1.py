class Solution():
    def leftshift(self,arr):
        n = len(arr)

        temp = arr[0]

        for i in range(1,n):
            arr[i-1] = arr[i]

        arr[n-1] = temp
        return arr
        


s1 = Solution()

arr = [1,2,3,4,5,6,7,8,8,9,0,1,0,10]

print(s1.leftshift(arr))