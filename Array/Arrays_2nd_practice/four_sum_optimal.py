class Solutuion():
    def fourSum(self,arr,target):
        n = len(arr)
        ans = []
        arr.sort()

        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue

            for j in range(i+1,n):

                if j > i+1 and arr[j] == arr[j-1]:
                    continue

                k = j+1
                l = n-1

                while k < l:
                    total_sum = arr[i]+ arr[j] + arr[k] + arr[l]

                    if total_sum == target:
                        ans.append([arr[i],arr[j],arr[k],arr[l]])

                        k += 1
                        l-=1

                        while k < l and arr[k] == arr[k-1]:
                            k+=1

                        while k < l and arr[l] == arr[l+1]:
                            l-=1

                    elif total_sum < target:
               
                        k+=1

                    else:
                        l-=1

        return ans

s1 = Solutuion()
print(s1.fourSum([1,-2,3,5,7,9],7))


                    