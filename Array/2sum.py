class SOlution():
    def twosum(self,arr):

        n = len(arr)

        target = 14

        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j] == target:
                    return arr[i],arr[j]

        
                    

        

s1 = SOlution()

arr = [2,6,5,8,11]

s1.twosum(arr)

print(s1.twosum(arr))