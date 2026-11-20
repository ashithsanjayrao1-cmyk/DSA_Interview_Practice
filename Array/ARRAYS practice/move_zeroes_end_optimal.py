class Solution():
    def MoveZeroes(self,arr):
        n = len(arr)

        j = 0
        i = 0

        for i in range(n):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]


                j += 1
                i += 1

                # if arr[i] == 0:
                #     i += 1

        return arr

s1 = Solution()
arr = [0,0,4,0,0,2]
print(s1.MoveZeroes(arr))
