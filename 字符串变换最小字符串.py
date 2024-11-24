#  -*-  coding: utf-8  -*-
# 接收原始字符串
# dcba
s = list(input())

# 将原始字符串排序
# acbd
s_sorted = sorted(s)

# 遍历原始字符串，对比排序后的字符串

# 找到该位置在原始字符串中的位置，交换原始字符串中当前位置和排序后的字符串在原始字符串中的位置
for i in range(len(s)):
    if s[i] != s_sorted[i]:
        position = s.index(s_sorted[i])
        s[i], s[position] = s[position], s[i]
    break
print(''.join(s))
