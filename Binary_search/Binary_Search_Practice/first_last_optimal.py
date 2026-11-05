class Solutionn():
    def first(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1

        first = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == x:
                first = mid
                high = mid-1

            elif arr[mid] < x:
                low = mid+1

            else:
                high = mid-1

        return first
    

    def last(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        last = -1

        while low<=high:
            mid =(low+high)//2
            if arr[mid] == x:
                last = mid
                low = mid+1

            elif arr[mid] < x:
                low = mid+1
            else:
                high = mid-1


        return last

    def fisrtLast(self,arr,x):

        first = self.first(arr,x)

        if first == -1:

            return [-1,-1]
        last = self.last(arr,x)

        return [first,last]


s1 = Solutionn()

arr = [3,4,4,7,8,10]
x = 4

print(s1.fisrtLast(arr,x))
    