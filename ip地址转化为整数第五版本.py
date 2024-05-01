# ip地址转化过程中，将字符串转化为数字的形式

from ip地址转化为整数第三版 import get_int32


def is_legal_ip(strs, length):
    # 判断ip的长度是否够4位
    if length != 4:
        return False

    # 判断第一位是否在区间内
    if 0 <= strs[0] <= 128:
        # 判断ip地址的每位是否在区间内
        for i in range(length-1):
            if 0 <= strs[i] <= 255:
                pass
            else:
                return False

    # 返回真
    return True


if __name__ == '__main__':
    s = input()

    try:
        strs = list(map(int, s.split('#')))
        length = len(strs)
        if is_legal_ip(strs, length):
            print(get_int32(strs, length))
        else:
            print('Invalid Ip')
    except:
        print('Invalid Ip')
        exit()






