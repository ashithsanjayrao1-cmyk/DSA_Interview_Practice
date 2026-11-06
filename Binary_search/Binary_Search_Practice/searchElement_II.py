class Solution():

    def searchElement(self,arr,target):

        n = len(arr)

        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == target:
                return True

            if arr[mid] == arr[low] and arr[mid] == arr[high]:
                low +=1
                high -= 1

                continue




            if arr[low] <= arr[mid]:
                if target >= arr[low] and target <=  arr[mid]:

                    high = mid-1

                else:

                    low = mid+1
            else:
                if target >= arr[mid] and target <= arr[low]:

                    low = mid-1
                else:
                    high = mid+1


        return False



s1 = Solution()

arr = [3,3,1,2,3,3,3,3,3]
        
print(s1.searchElement(arr,10))