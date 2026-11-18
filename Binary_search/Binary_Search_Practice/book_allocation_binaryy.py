class Solution():
    def func(self,arr,page_limit):
        students = 1

        current_page = 0
        n = len(arr)

        for i in range(n):
            if current_page + arr[i] > page_limit:

                students += 1
                current_page = arr[i]

            else:

                current_page += arr[i]

        return students

    def binary_search(self,arr,m):

        low = max(arr)
        high = sum(arr)

        while low <= high:
            mid = (low+high)//2

            count_student = self.func(arr,mid) 

            if count_student < m:

                high = mid-1
            else:
                low = mid+1

        return low
s1 = Solution()
arr = [2,3,4,5,9]

print(s1.binary_search(arr,4))
            
        