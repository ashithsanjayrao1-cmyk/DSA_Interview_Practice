class Solution():
    def moveZeroes(self,arr):
        n = len(arr)

        temp = []

        for i in range(n):
            if arr[i] != 0:
                temp.append(arr[i])

        for i in range(len(temp)):
            arr[i] = temp[i]

        for i in range(len(temp),n):

            arr[i] = 0

        return arr
    

s1 = Solution()

arr = [0,1,4,0,5,2]

print(s1.moveZeroes(arr))

        