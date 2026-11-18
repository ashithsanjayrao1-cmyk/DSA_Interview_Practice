class SOlution():
    def pascal(self,n,r):

        res = 1

        for i in range(r):

            res = res * (n-i)

            res = res//(i+1)

        return res

    def print(self,row,col):

        return self.pascal(row-1,col-1)

s1 = SOlution()
r = 5
c = 3
print(s1.print(r,c))
