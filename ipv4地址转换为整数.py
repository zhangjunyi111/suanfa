

s = input()

# 判断是否存在空串

strs = s.split('#')
length = len(strs)
if length != 4:
    print('存在空串')

# 判断每个字段是否都是数字

for i in range(length):
    if strs[i].isdigit():
        continue
    else:
        print('存在非法字符')

# 判断是否在合法区间

for i in range(length):
    if i == 0:
        if 0 <= int(strs[i]) <= 128:
            continue
        else:
            print("不在合理范围内")
    else:
        if 0 <= int(strs[i]) <= 255:
            continue
        else:
            print('不在合法区间')

# print(65536*16)
# print(int('64650105', 16))

hexstrings = ''

for i in range(len(strs)):
    x = hex(int(strs[i]))[2:]
    if len(x) == 1:
        x = '0'+x
    hexstrings += x

res = int(hexstrings, 16)
print(res)
