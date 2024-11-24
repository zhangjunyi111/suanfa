#  -*-  coding: utf-8  -*-

# 接收原始字符串和数字
original_string, N = input().split()

# 对原始字符串进行去重
duplite_list = list(set(original_string))

res = []
used = [False] * len(duplite_list)
str = ''


def generate_str(used, str, i):
    if len(str) == int(N):
        res.append(str)
        return
    for i in range(len(duplite_list)):
        if used[i]:
            continue
        used[i] = True
        generate_str(used, str+duplite_list[i], i)
        used[i] = False


generate_str( used, '', 0)
print(len(res))
