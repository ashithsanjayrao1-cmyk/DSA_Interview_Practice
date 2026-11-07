class SolutioN():
    def majorityElement(self,arr):
        n= len(arr)

        treshold = (n//3)+1

        ans = []

        map = {}

        for i in range(n):
            map[arr[i]] = map.get(arr[i],0) + 1
            if map[arr[i]] == treshold:
                ans.append(arr[i])

            if len(ans) == 2:
                break

            

        return ans



s1 = SolutioN()

arr = [1,1,1,1,3,2,2,2]

print(s1.majorityElement(arr))
            