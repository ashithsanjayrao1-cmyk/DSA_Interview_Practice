class Solution():
    def majorityelement(self,arr):
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
                count -= 1
        v_count = 0
        for i in range(n):
            if arr[i] == el:
                v_count += 1

        if v_count > n // 2:
            return el

        return -1
    
        # hash_map = {}

        # for i in range(n):
        #     if arr[i] in hash_map:
        #         hash_map[arr[i]] += 1

        #     else:
        #         hash_map[arr[i]] = 1

        #     if hash_map[arr[i]] > n // 2:
        #         return arr[i]

            

        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if arr[i] == arr[j]:
        #             count += 1

        #     if count > n // 2:
        #         return arr[i]


s1 = Solution()

arr = [1,1,2,3,4,1,2,1,1,1]

print(s1.majorityelement(arr))
                    