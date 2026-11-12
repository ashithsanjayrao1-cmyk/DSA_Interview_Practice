class SolutioN():
    def maxOnes(self,arr):

        n = len(arr)
        max = 0
        count = 0 


        for i in range(n):

            if arr[i] == 1:
                count += 1

                if max < count:
                    max = count

            else:
                count = 0

        return max

s1 = SolutioN()

arr = [1,1,0,0,1,1,1,0]

print(s1.maxOnes(arr))