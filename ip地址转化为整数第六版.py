# 将map函数映射完的结果移动到内部进行比较

from ip地址转化为整数第三版 import get_int32


def is_legal_ip(s):
    # 判断ip的长度是否够4位
    arr = s.split('#')
    if len(arr) != 4:
        return False
    ipv1, ipv2, ipv3, ipv4 = map(int, arr)
    if 0 <= ipv1 <= 128 and 0 <= ipv2 <= 255 and 0 <= ipv3 <= 255 and 0 \
            <= ipv4 \
            <= 255:
        return True
    else:
        return False


if __name__ == '__main__':
    s = input()
    length = len(s.split('#'))
    try:
        if is_legal_ip(s):
            print(get_int32(s.split('#'), length))

    except:
        print('Invalid Ip')
        exit()






