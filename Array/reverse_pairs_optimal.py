class Solution():
    def count_pairs(self,arr,low,mid,high):

        right = mid + 1
        count = 0

        for i in range(low,mid+1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1

            count += (right - (mid+1))

        return count

    def merge_sort(self,arr,low,high):

        if low >= high:
            return 0 

        mid = (low + high) // 2
 
        count = 0


        count += self.merge_sort(arr,low,mid)

        count += self.merge_sort(arr,mid+1,high)

        count += self.count_pairs(arr,low,mid,high)

        self.merge(arr,low,mid,high)

        return count


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

    def reverse_pairs(self,arr):
        return self.merge_sort(arr,0,len(arr)-1)
    
s1 = Solution()
my_array = [40,25,19,12,6,2]

final_count = s1.reverse_pairs(my_array)
print(final_count)
        
    