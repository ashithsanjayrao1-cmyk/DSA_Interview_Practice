class Solution():
    def twoSum(self,arr,target):
        n = len(arr)
        hash_map = {}

        for i in range(n):
            current_sum = arr[i]
            needed = target - current_sum

            if needed in hash_map:
                return [hash_map[needed],i]
            hash_map[current_sum] = i
        return [-1,-1]

s1 = Solution()
print(s1.twoSum([1,6,2,10,3],7))