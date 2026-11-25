class Solution():
    def majorityElement(self,arr):
        n = len(arr)
        hash_map = {}
        result = []
        threshold = n//3

        for i in range(n):
            num = arr[i]

            hash_map[num] = hash_map.get(num,0) + 1

            if hash_map[num] == threshold + 1:
                result.append(num)
            if len(result) == 2:
                break
        return result
s1 = Solution()
print(s1.majorityElement([1,2,1,3,4,1]))
            
