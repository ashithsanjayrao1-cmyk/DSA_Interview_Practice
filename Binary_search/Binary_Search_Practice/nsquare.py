class Soution():

    def multiply(self,mid,n,m):
        ans = 1

        for i in range(1,n+1):
            ans = ans*mid

            if ans > m:
                return 2
        if ans == m:
            return 1

        else:
            return 0
              
     


    def nRoot(self,n,m):

        low = 1
        high = m-1

        while low<=high:
            mid = (low+high)//2

            val = self.multiply(mid,n,m)

            if val == 1:
                return mid

            elif val == 0:
                low = mid+1
            else:
                high = mid-1

        return -1


s1 = Soution()

print(s1.nRoot(3,27))