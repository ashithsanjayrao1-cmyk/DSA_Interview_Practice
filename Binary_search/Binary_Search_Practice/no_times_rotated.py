class Solution():
    def totated(self,arr):
        n = len(arr)
        low = 0
        high = n-1
        index = -1

        ans = float('inf')


        while (low<=high):
            mid = (low+high)//2

            if arr[low]<=arr[mid]:

                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                low = mid+1

            else:

                if arr[mid] < ans:

                    ans = arr[mid]

                    index = mid
                high = mid-1

        return index


s1 = Solution()

arr = [4,5,6,7,0,1,2,3]

print(s1.totated(arr))
