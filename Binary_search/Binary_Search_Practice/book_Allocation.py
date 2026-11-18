class SOlution():
    def func(self,arr,page_limit):
        student = 1
        current_page = 0
        n = len(arr)

        for i in range(n):
           
           

            if current_page + arr[i] > page_limit:

               student += 1
               current_page = arr[i]

            else:

               current_page += arr[i]

        return student


    def linearSearch(self,arr,m):

        low = max(arr)
        high = sum(arr)

        if m > len(arr):
            return -1
        


        for i in range(low,high+1):

            count_student = self.func(arr,i)

            if count_student <= m:
                return i

        return -1
s1 = SOlution()

arr = [2,3,4,5,9]

print(s1.linearSearch(arr,4))
            
               