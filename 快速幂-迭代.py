# 问题：求pow(x,n)

# 迭代的思想需要将十进制的n转化为二进制的n
# 然后需要找出n中二进制位为1的位数，从右向左数，第一个位置为0
# 比如二进制为 1101110111,那么i0 =1  i1=1 i2 =1 i3=0

# print(bin(10)[2:])


# 由于遍历的时候是从右往左遍历的，所以需要将二进制字符串翻转

# 遍历并统计哪些位数为1，统计到数组中，isone

# 遍历数组 isone,，求pow(2, isone)

# 从x开始不断地进行平方运算，如果结果在isone数组里面，就乘上它，否则不乘


class Solution:
    def myPow(self, x, n):
        ans = 1
        tmp = bin(n)[2:][::-1]
        for i in range(len(tmp)):
            if int(tmp[i]) == 1:
                ans *= x
            x *= x
        return  ans

s = Solution()
print(s.myPow(2,10))