class SolutioN():
    def lowerBound(self,arr,x):
        n = len(arr)
        low = 0 
        high = n-1
        ans = n

        while low<=high:
            mid = (low+high)//2
            if arr[mid] >= x:
                ans = mid
                high = mid-1

            else:
                low =mid+1

        return ans

    def upperBound(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1

        ans = n


        while low<=high:
            mid =(low+high)//2

            if arr[mid] > x:
                ans = mid
                high  = mid-1

            else:
                low = mid+1

        return ans

    def firstLast(self,arr,x):
        n=len(arr)

        lb = self.lowerBound(arr,x)

        if lb == n or arr[lb] != x:
            return [-1,-1]
        ub = self.upperBound(arr,x)

        return[lb,ub-1]

s1 = SolutioN()

arr = [3,4,4,7,8,10]
x = 4

print(s1.firstLast(arr,x))