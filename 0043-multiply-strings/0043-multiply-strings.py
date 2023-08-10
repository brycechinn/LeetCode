class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # approach: elementary multiplication, reverse nums then
        # update res at (i + j)th index
        
        if '0' in [num1, num2]:
            return '0'
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                prod = int(num1[i]) * int(num2[j])
                res[i + j] += prod
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res, start = res[::-1], 0
        while res[start] == 0 and start < len(res):
            start += 1
        
        return ''.join([str(i) for i in res[start:]])