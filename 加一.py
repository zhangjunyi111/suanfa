from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 先把整数从数组中读取出来

        digits =list(map(lambda  x: str(x), digits))
        if len(digits) > 1:
            num = int(''.join(digits))
        else:
            num = int(digits[0])

        # 执行+1 操作
        newnum = num + 1

        strnum = str(newnum)

        res = []
        for i in range(len(strnum)):
            res.append(strnum[i])
        return res


s = Solution()
print(s.plusOne([1,2,3]))