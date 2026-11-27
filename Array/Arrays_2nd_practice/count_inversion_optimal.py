class Solution():
    def merge_sort(self,arr,low,high):

        count = 0

        if low >= high:
            return count

        mid = (low+high)//2


        count += self.merge_sort(arr,low,mid)
        count += self.merge_sort(arr,mid+1,high)
        count += self.merge(arr,low,mid,high)
        return count

    def merge(self,arr,low,mid,high):
        temp = []
        count = 0
        left = low

        right = mid+1

        while left <= mid and right <=high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])

                left+=1
            else:
                count += (mid-left+1)
                temp.append(arr[right])
                right +=1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right+=1
        for i in range(len(temp)):
            arr[low+i] = temp[i]

        return count

    def count_inversion(self,arr):
        return self.merge_sort(arr,0,len(arr)-1)

        

s1 = Solution()
print(s1.count_inversion([2,3,7,1,3,5]))
