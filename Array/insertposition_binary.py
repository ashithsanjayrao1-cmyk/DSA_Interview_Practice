class Solution():
    def insertposition(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        ans = n

        while low<= high:
            mid = (low+high)//2

            if arr[mid]>x:
                ans = mid
                high = mid-1

            else:
                low = mid+1


        return ans

s1 = Solution()
nums = [1, 2, 4, 4, 6, 8, 10]
x = 9

print(s1.insertposition(nums,x))
