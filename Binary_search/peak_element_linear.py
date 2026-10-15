class Solution():
    def findPeakElement(self,arr):
        n = len(arr)

        if n == 1:
            return 0 

        for i in range(n):
            if i == 0:
                if arr[i] > arr[i+1]:
                    return i

            elif i == n-1:
                if arr[i] > arr[i-1]:
                    return i 

            else:
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    return i

        return -1

s1 = Solution()

arr = [1,2,3,4,5,6,8,5,4,3,2,1]


print(s1.findPeakElement(arr))
    
