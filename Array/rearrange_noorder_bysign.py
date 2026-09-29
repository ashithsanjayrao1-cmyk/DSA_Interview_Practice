class Solution():
    def rearrangearray(self,arr):
        n = len(arr)

        pos = []
        neg = []

        for i in range(n):
            if arr[i] > 0:
                pos.append(arr[i])

            else:
                neg.append(arr[i])

        if len(pos) < len(neg):
            for i in range(len(pos)):
                arr[2 * i] = pos[i]
                arr[2 * i + 1] = neg[i]


            idx = len(pos) * 2
            for i in range(len(pos), len(neg)):
                arr[idx] = neg[i]
                idx += 1

        else:

            for i in range(len(neg)):
                arr[2 * i] = pos[i]
                arr[2 * i + 1] = neg[i]

            idx = len(neg) * 2

            for i in range(len(neg), len(pos)):
                arr[idx] = pos[i]
                idx += 1


        return arr

s1 = Solution()

arr = [1, 2, -4, -5, 3, 4] 

print(s1.rearrangearray(arr))

