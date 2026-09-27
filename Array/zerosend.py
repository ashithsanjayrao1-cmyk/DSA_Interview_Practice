class Solution():

    # def zerosend(self,arr):
    #     n = len(arr)
    #     temp = []


        # for i in range(n):
        #     if arr[i] != 0:
        #         temp.append(arr[i])

        # nz_count = len(temp)

        # for i in range(nz_count):
        #     arr[i] = temp[i]

        # for i in range(nz_count,n):

        #     arr[i] = 0

        # return arr

    def zerosend(self,arr):
        n = len(arr)

        j = -1

        for i in range(n):
            if arr[i] == 0:
                j = i
                break

        if j == -1:
            return arr

        for i in range(j+1,n):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]

                j+=1

        return arr



s1 = Solution()

arr = [1,0,2,3,0,4,1,0,3,0]

print(s1.zerosend(arr))

            

    