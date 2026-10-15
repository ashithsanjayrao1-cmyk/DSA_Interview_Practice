class Solution():
    def countStudents(self,arr,page_limit):
        students = 1
        current_page = 0

        for book in arr:
            if current_page + book > page_limit:
                students += 1
                current_page = book
            else:
                current_page += book

        return students


    def findPages(self,arr,n,m):
        if m>n:
            return -1

        low = max(arr)

        high = sum(arr)

        ans = -1

        while low <= high:
            mid = (low+high)//2


            if self.countStudents(arr,mid) <= m:
                ans = mid
                high = mid-1
            else:
                low = mid+1


        return ans

s1 = Solution()
arr = [12, 34, 67, 90]
n = 4 
m = 2 

print(s1.findPages(arr,n,m))

