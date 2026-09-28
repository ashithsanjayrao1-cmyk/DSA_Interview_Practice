class Solution():
    def removeduplicate(self,arr):

        n = len(arr)
        i = 0

        for j in range(n):

            if arr[j] != arr[i]:
                arr[i+1] = arr[j]
                i +=1   

        return i+1





    
    

s1 = Solution()

arr = [1,1,2,2,3,3,4,4]

print(s1.removeduplicate(arr))
