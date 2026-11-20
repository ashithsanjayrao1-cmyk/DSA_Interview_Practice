class Solution():
    def twoSum(self,arr,target):
        n = len(arr)

        hashmap = {}

        for i in range(n):
            current = arr[i]
            actual = target - current

            if actual in hashmap:
                return[hashmap[actual],i]

            hashmap[current] = i

        return [-1,-1]


s1 = Solution()
target = 7
arr = [1,6,2,10,3]

print(s1.twoSum(arr,target))