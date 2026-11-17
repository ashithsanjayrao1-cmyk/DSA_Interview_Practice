class Solution():
    def rearrange(self,arr):
        n = len(arr)

        pos = []
        neg = []

    

        for i in range(n):
            if arr[i] > 0:
                pos.append(arr[i])

            else:
                neg.append(arr[i])

        if len(pos) > len(neg):

            for i in range(len(neg)):
                arr[2*i] = pos[i]
                arr[2*i+1] = neg[i]

            idx = len(neg) * 2

            for i in range(len(neg),len(pos)):

                arr[idx] = pos[i]

                idx+=1
        else:

            for i in range(len(pos)):

                arr[2*i] = pos[i]
                arr[2*i+1] = neg[i]

            index = len(pos) * 2

            for i in range(len(pos),len(neg)):

                arr[idx] = neg[i]
                index += 1

        return arr

s1 = Solution()
print(s1.rearrange([2,4,5,-1,-3,-4]))







                

