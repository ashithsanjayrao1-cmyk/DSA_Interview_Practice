class Solution():
    def threesum(self,arr):

        ans = []
        n = len(arr)

        arr.sort()


        for i in range(n):
            if i != 0 and arr[i] == arr[i-1]:
                continue

            j = i+1
            k = n-1

            while j<k:
                total_sum = arr[i] + arr[j] + arr[k]

                if total_sum < 0:
                    j +=1
                elif total_sum > 0:
                    k-=1

                else:
                    ans.append([arr[i],arr[j],arr[k]])

                    j +=1
                    k -=1

                    while j < k and arr[j] == arr[j-1]:

                        j += 1

                    while j < k and arr[k] == arr[k+1]:

                        k -= 1

        return ans

s1 = Solution()
arr = [-1, 0, 1, 2, -1, -4]
print(s1.threesum(arr))


