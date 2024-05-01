# 1.将get_int32 和is_legal_ip合并为一个函数
# 2.第七版程序将那个生成十六进制的过程提取成一个函数，四个ip字段都需要先转化为16进制，再进行相加，因此转化为
# 十六进制很关键，是可以做成公共函数的

# 3.这里有一个疑问，为什么这里转化为十六进制的的时候，如果只有1位，需要在前面补0？
# 4.return 返回函数操作，这点可以学习
# 5.引入异常捕获语句，在函数中，执行map操作，进行异常捕获，这需要对map很熟悉才能用的上，对异常很熟悉，难度比较大，

from ip地址转化为整数第三版 import get_int32


def get_hex(num):
    hexstring = hex(num)[2:]
    if len(hexstring) == 1:
        hexstring = '0' + hexstring
    return hexstring


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
    s = input()
    print(get_result(s))
