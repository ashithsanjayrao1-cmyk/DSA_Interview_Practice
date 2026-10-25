class Solution():
    def leftRotateArray(self,arr):
        n = len(arr)
        temp = arr[0]

        for i in range(1,n):


            arr[i-1] = arr[i]

            i += 1

            

        arr[n-1] = temp

        return arr
    


s1 = Solution()

arr = [1,2,3,4,5]

print(s1.leftRotateArray(arr))

