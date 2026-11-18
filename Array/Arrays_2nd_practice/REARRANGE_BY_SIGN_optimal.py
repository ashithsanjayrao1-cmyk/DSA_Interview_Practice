class SOlution():
    def Rearrange(self,arr):
        n = len(arr)

        pos = []
        neg = []


        for i in range(n):

            if arr[i] > 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])

        p = len(pos)
        ni = len(neg)




        if p > ni :
            for i in range(ni):

                arr[2*i] = pos[i]
                arr[2*i+1] = neg[i]

            index = ni*2

            for i in range(ni,p):
                arr[index] = pos[i]
                index +=1

        else:
            for i in range(p):
                arr[2*i] = pos[i]
                arr[2*i+1] = neg[i]
            index = p*2

            for i in range(p,ni):
                arr[index] = neg[i]
                index +=1


        return arr
s1 = SOlution()

arr = [3,1,-2,-5,-4,-4,-4,-4]

print(s1.Rearrange(arr))

