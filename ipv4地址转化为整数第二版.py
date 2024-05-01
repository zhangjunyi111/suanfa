# 将print语句中的语句转化为英文单词

s = input()

# 判断是否存在空串

strs = s.split('#')
length = len(strs)
if length != 4:
    print('invalid IP')

# 判断每个字段是否都是数字

for i in range(length):
    if strs[i].isdigit():
        continue
    else:
        print('invalid IP')

# 判断是否在合法区间

for i in range(length):
    if i == 0:
        if 0 <= int(strs[i]) <= 128:
            continue
        else:
            print("invalid IP")
    else:
        if 0 <= int(strs[i]) <= 255:
            continue
        else:
            print('invalid IP')

hexstrings = ''

for i in range(len(strs)):
    x = hex(int(strs[i]))[2:]
    if len(x) == 1:
        x = '0'+x
    hexstrings += x

res = int(hexstrings, 16)
print(res)

