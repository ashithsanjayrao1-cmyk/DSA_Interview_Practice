class Solution():
    def arrayRotated(self,arr):
        n = len(arr)

        low = 0 
        high = n-1

        ans = float('inf')

        index = -1

        while low<=high:
            mid = (low+high)//2

            if arr[low] <= arr[high]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                    break

            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                low = mid+1

            else:
                if arr[mid]<ans:
                    ans = arr[mid]
                    index = mid

                high = mid-1

        return index
    
s1 = Solution()

arr1 = [1, 2, 3,4,5]

arr2 = [3,4,5,1,2]

print(s1.arrayRotated(arr1))

