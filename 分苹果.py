import sys

# 读取苹果的数量
n = int(input())

# 读取每个苹果的重量
weights = list(map(int, input().split()))

# 初始化一个最小的苹果的重量
min_weigh = sys.maxsize
sum_ = 0
for wei in weights:
    sum_ = sum_ ^ wei
    if wei < min_weigh:
        min_weigh = wei

if sum_ == 0:
    print(sum(weights) - min_weigh)

else:
    print(-1)
