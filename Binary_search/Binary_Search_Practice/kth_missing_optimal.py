class Solution():
    def binarysearch(self,arr,k):

        n = len(arr)
        low = 0
        high = n-1

        while low <= high:
            mid = (low+high)//2

            missing = arr[mid] - (mid+1)
            if missing < k:
                low = mid+1

            else:
                high = mid-1

        return k+low
s1 = Solution()
print(s1.binarysearch([3,5,7,10],6))