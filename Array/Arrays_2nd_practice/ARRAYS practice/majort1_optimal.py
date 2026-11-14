class Solution():
    def majority(self,arr):

        n = len(arr)

        count = 0

        el = None

        for i in range(n):
            if count == 0:
                count = 1

                el = arr[i]

            elif arr[i] == el:
                count += 1

            else:
                count-=1

        v_count = 0

        for i in range(n):
            if arr[i] == el:
                v_count += 1

        if v_count > n//2:
            return el
        return -1


s1 =Solution()

arr = [7,0,0,1,7,7,2,7,7]
print(s1.majority(arr))


        


