class Solution():
    def binarySearchRecursive(self,arr,low,high,target):

        if low > high:
            return -1

        mid = (low+high) //2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return self.binarySearchRecursive(arr,low,mid-1,target)

        else:
            return self.binarySearchRecursive(arr,mid+1,high,target)


    def search(self,arr,target):
        return self.binarySearchRecursive(arr,0,len(arr)-1 , target)


s1 = Solution()

target = 4

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(s1.search(arr, target))
