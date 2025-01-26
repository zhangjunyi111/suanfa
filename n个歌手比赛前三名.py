import sys

# 输入
# m代表评委的数量
# n代表选手的数量
m, n = map(int, input().split(','))
sorces = []
for i in range(m):
    sorces.append(list(map(int, input().split(','))))

# 排除异常情况
if m < 3 or m > 10 or n < 3 or n > 100:
    print(-1)
    sys.exit()

players = {}

# 构造字典，键为选手的序号，值为选手的得分
for i in range(n):
    playerscore = [row[i] for row in sorces]
    playerscore.sort(reverse=True)
    players[i] = playerscore

print(sorces)
print('players',players)

# 对字典进行排序
players = sorted(players.items(),key=lambda x:(sum(x[1]),x[1]),reverse=True)
# print()
# for x in players.items():
#     print(x)
top3player =players[:3]
result  = [player[0] +1 for player in top3player]
print(','.join(result))
# print(players)
# 构造输出结果，输出
