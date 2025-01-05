# 获取商品数量
goods_numbers = int(input())
# 获取出售天数
days = int(input())
# 获取最大持有量
max_limits = list(map(int, input().split()))
# 初始化价格数组，获取每件商品，每天的价格
prices = []

for i in range(goods_numbers):
    prices.append(list(map(int, input())))

# 遍历每件商品，计算哪天盈利了，加入到利润里面去，然后在最大的商品数量乘积
total_profit = 0
for i in range(goods_numbers):
    profit = 0
    for j in range(1, days):
        if prices[i][j] - prices[i][j - 1] > 0:
            profit += prices[i][j] - prices[i][j - 1]
    profit *= max_limits[i]
    total_profit += profit

print(total_profit)