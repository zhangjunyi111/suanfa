# date:20240128
# 优化get_hex函数
from ip地址转化为整数第七版 import get_result


def get_hex(num):
    return '{:02x}'.format(num)


def get_result(s):
    # 判断ip的长度是否够4位
    arr = s.split('#')
    if len(arr) != 4:
        return False
    try:
        ipv1, ipv2, ipv3, ipv4 = map(int, arr)
        if 0 <= ipv1 <= 128 and 0 <= ipv2 <= 255 and 0 <= ipv3 <= 255 and 0 \
                <= ipv4 \
                <= 255:
            hexstring = get_hex(ipv1) + get_hex(ipv2) + get_hex(ipv3) + \
                        get_hex(ipv4)
            return int(hexstring, 16)
        else:
            return False
    except Exception as e:
        print('Invalid Ip')


if __name__ == '__main__':
    get_result()