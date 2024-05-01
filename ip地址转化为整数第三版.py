# 将return语句中的语句转化为英文单词


# 梳理出2个函数，is_legal_ip和 get_int_32 2个函数，如果第一个函数的返回值为True,才会进行第二个函数，
# 否则直接返回False

def is_legal_ip(strs,length):
    # 判断ip的长度是否够4位
    if length != 4:
        return('False')
    # 判断每个字段是否都是数字
    for i in range(length):
        if strs[i].isdigit():
            pass
    # 判断是否在合法区间
        if i == 0:
            if 0 <= int(strs[i]) <= 128:
                pass
            else:
                return('False')
        else:
            if 0 <= int(strs[i]) <= 255:
                pass
            else:
                return('False')
    return 'True'


def get_int32(strs, length):
    hexstrings = ''
    for i in range(length):
        x = hex(int(strs[i]))[2:]
        if len(x) == 1:
            x = '0' + x
        hexstrings += x

    res = int(hexstrings, 16)
    return(res)


if __name__ == '__main__':
    s = input()
    # 判断是否存在空串
    strs = s.split('#')
    length = len(strs)
    if is_legal_ip():
        res = get_int32(strs, length)
        print(res)
    else:
        print('Invalid Ip')
    