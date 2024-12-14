# 报文重排序
# 例子
# 8
# gifts6 and7  Exchanging1 all2 precious5 things8 kinds3 of4
#
# //  注：这里需要注意:and7与Exchanging1有两个空格


def main():
    # 接收报文数量N
    N = int(input())

    # 接收报文字符串
    messages = input().strip().split()

    # 初始化一个报文字典
    message_dict = dict()

    # 对报文字符串做初步处理，将每个报文先取到，再将报文中的数字和字母区分开

    for message in messages:
        for i in range(len(message)):
            ch = message[i]
            # 找到数字部分，将数字和字母切开分别赋值给不同的变量，然后保存到字典中
            if ch.isdigit():
                index = int(i)
                message_sequence = int(message[index:])
                message_content = message[:index]
                message_dict[message_sequence] = message_content

    # print(message_dict)
    # 按顺序打印报文
    for i in range(1,N+1):
        print(message_dict[i], end=' ')

main()