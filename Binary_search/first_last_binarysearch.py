class SOlution():
    def first(self,arr,target):

        n = len(arr)

        low = 0

        high = n-1

        first = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == target:
                    first = mid
                    high = mid-1


            elif arr[mid] > target:
                high = mid -1

            else:

                low = mid+1

        return first


    def last(self,arr,target):

         n = len(arr)

         low = 0
         high = n-1

         last = -1

         while low<=high:
              mid = (low+high)//2


              if arr[mid] == target:
                   last = mid
                   low = mid+1
              elif arr[mid] < target:
                   low = mid+1

              else:
                   high = mid-1

         return last

    def firstLast(self,arr,x):
         n = len(arr)

         firstoccur = self.first(arr,x)

         if firstoccur == -1:
              return [-1,-1]

         lastOccur = self.last(arr,x)

         return [firstoccur,lastOccur]


s1 = SOlution()

arr = [2, 4, 6, 11, 13]

print(s1.firstLast(arr,8))


