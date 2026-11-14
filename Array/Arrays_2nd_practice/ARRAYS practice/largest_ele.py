class Solutoion():
    def Largest(self,arr):

        n = len(arr)

        largest = arr[0]

        for i in range(n):

            if arr[i] > largest:
                largest = arr[i]


        return largest


s1 = Solutoion()

arr = [3,3,6,1]

print(s1.Largest(arr))