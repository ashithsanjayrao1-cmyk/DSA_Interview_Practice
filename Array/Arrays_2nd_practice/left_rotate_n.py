class Solution():
    def rotateByN(self,arr,d):
        n = len(arr)

        d = d%n

        temp = []

        for i in range(d):
            temp.append(arr[i])

        for i in range(d,n):
            arr[i-d] = arr[i]

        for i in range(d):
            arr[n-d+i] = temp[i]
        return arr

s1 = Solution()

arr = [1,2,3,4,5]

print(s1.rotateByN(arr,2))