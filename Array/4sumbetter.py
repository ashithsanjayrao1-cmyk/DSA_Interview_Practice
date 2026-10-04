class Solutiion():
    def foursum(self,arr,target):
        n = len(arr)

        unique_quads = set()

        for i in range(n):
            for j in range(i+1,n):

                seen_elements = set()

                for k in range(j+1,n):

                    needed = target - (arr[i] + arr[j] + arr[k])

                    if needed in seen_elements:
                        temp = [arr[i],arr[j],arr[k],needed]

                        temp.sort()

                        unique_quads.add(tuple(temp))

                    seen_elements.add(arr[k])

        ans = [list(quad) for quad in unique_quads]

        return ans

s1 = Solutiion()
arr = [1, 0, -1, 0, -2, 2]
target = 0
print(s1.foursum(arr, target))
    


    

