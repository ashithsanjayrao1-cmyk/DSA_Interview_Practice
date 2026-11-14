class Solution():
    def majority(self,arr):
        n = len(arr)

        hash = {}

        for num in arr:
            if num in hash:
                hash[num] += 1

            else:
                hash[num] = 1


            if hash[arr[num]] > n//2:
                return arr[num]

        return -1

     


s1 =Solution()

arr = [7,0,0,1,7,7,2,7,7]
print(s1.majority(arr))
    