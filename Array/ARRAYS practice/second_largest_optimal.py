class Solution():
    def secondLargest(self,arr):
        n = len(arr)

        if n < 2:
            return -1
        
        largest = arr[0] 
        sLargest = float('-inf')

        for i in range(1,n):
            if arr[i] > largest:
                sLargest = largest
                largest = arr[i]
            elif arr[i] > sLargest and arr[i] != largest:
                sLargest = arr[i]

        if sLargest == float('-inf'):
            return -1

        return sLargest
        

s1 = Solution()
arr = [3,3,6,-1]

print(s1.secondLargest(arr))

                