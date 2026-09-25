class Solution():
    def merge_sort(self,arr,low,high):

        if low >= high:
            return

        mid = (low + high) // 2


        self.merge_sort(arr,low,mid)

        self.merge_sort(arr,mid+1,high)

        self.merge(arr,low,mid,high)


    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid+1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])

                left += 1

            else:
                temp.append(arr[right])

                right += 1
                          
        while left <= mid:
            temp.append(arr[left])
            left += 1


        while right <= high:
            temp.append(arr[right])

            right += 1

        for i in range(len(temp)):
            arr[low+i] = temp[i]
s1 = Solution()
my_array = [10, 4, 5, 7, 8, 2, 1]

s1.merge_sort(my_array, 0, len(my_array) - 1)
print(my_array)

        
    