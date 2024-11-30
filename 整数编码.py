# 接收带编码的字符
to_be_encode = int(input())

# 初始化一个数组，接收转化完成的字节
encodeed = []

# 转化为二进制
to_be_encode_bin = bin(to_be_encode)[2:]

# 每隔7位进行分组
for i in range(len(to_be_encode_bin), -1, -7):
    # 处理好当i和最后一位的间距的大小不够1时的情况
    if i - 7 <= 0:
        # 这种情况下不加1
        encodeed.append(to_be_encode_bin[:i])
        break
    tmp = to_be_encode_bin[i - 7:i]
    # 判断第八位加0还是加1
    tmp = str(1) + tmp
    encodeed.append(tmp)

# 小端序，先存储小端的
def bin_to_hex(binString):
    '''
    :param binString: 二进制字符串
    :return: 十六进制字符串
    '''
    return hex(int(binString,2))


# 右对齐的函数rjust
# 大写函数upper
# 二进制转化为十六进制 hex(int(2,x))
res = [bin_to_hex(x)[2:].upper().rjust(2,'0') for x in encodeed]
print(''.join(res))