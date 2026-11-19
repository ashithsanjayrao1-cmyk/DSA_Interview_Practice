class Soution():
    def pascalTriangle3(self,n):

        ans_val = 1
        ans = [1]

        for i in range(1,n):
            ans_val = ans_val*(n-i)
            ans_val = ans_val//i
            ans.append(ans_val)

        return ans
s1 = Soution()
print(s1.pascalTriangle3(6))