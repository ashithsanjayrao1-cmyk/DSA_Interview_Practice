class Solution():

    def moveZeroes(self,arr):
        n = len(arr)
        temp = []

        for i in range(n):
            if arr[i] != 0:
                temp.append(arr[i])

        nz = len(temp)

        for i in range(nz):

            arr[i] = temp[i]
        

        for i in range(nz,n):
            arr[i] = 0

        return arr
        
s1 = Solution()
print(s1.moveZeroes([1,0,2,0,3,4,0,6,0]))
