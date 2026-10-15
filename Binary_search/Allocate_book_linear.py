class Solution():
    def countStudents(self,arr,pahge_limit):
        students = 1
        current_page = 0

        for book in arr:
            if current_page + book > pahge_limit:
                students +=1
                current_page = book

            else:
                current_page += book

        return students

    def findPages(self,arr,n,m):

        if m>n:
            return -1

        low = max(arr)
        high = sum(arr)

        for pages in range(low , high+1):
            if self.countStudents(arr,pages) <= m:
                return pages

        return -1


s1 = Solution()
arr = [12, 34, 67, 90]

n = 4
m = 2


print(s1.findPages(arr,n,m))

    