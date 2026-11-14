class Solution():
    def move_zeroes(self,arr):
        n = len(arr)

        j = -1

        for i in range(n):
            if arr[i] == 0:
                j = i
                break

        for i in range(j+1,n):
            if arr[i]!= 0:
                arr[i],arr[j] = arr[j],arr[i]
                j+=1

        return arr

s1 = Solution()
print(s1.move_zeroes([1,0,2,0,3,4,0,4,5,87,9,0,1]))