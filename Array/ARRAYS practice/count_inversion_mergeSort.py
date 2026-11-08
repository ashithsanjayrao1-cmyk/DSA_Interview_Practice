class Solution():
    def merge(self,arr,low,mid,high):

        temp = []
        left = low 
        right = mid+1
        count = 0


        while left <= mid and right <= high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1

            else:

                temp.append(arr[right])
                count += (mid - left+1)
                right+=1

        while left <= mid:
            temp.append(arr[left])

            left+=1

        while right <= high:
            temp.append(arr[right])
            right +=1

        for i in range(len(temp)):
            arr[low+i] = temp[i]

        return count
    


    def mergeSort(self,arr,low,high):

        while low >= high:
            return


        mid = (low+high)//2

        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)


s1 = Solution()

arr = [2,3,7,1,3,5]


print(s1.mergeSort(arr))

        

