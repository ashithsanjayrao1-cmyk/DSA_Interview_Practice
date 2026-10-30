class Solution():
    def rearrange(self,arr):

        n = len(arr)

        pos = []
        neg = []

        for num in arr:
            if num > 0:
                pos.append(num)

            else:
                neg.append(num)

        for i in range(len(pos)):
            arr[2*i] = pos[i]

            arr[2*i+1] = neg[i]

        return arr

s1 = Solution()

arr = [2,4,5,-1,-3,-4]

print(s1.rearrange(arr))