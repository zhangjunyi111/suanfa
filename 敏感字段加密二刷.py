# 敏感字段加密
# 1
# password__a12345678_timeout_100
def main():
    '''
    :return:
    '''
    # 接收索引值
    K = int(input())

    # 接收输入字符串
    s = input()

    # 将字符串转化为数组
    s = list(s)

    # 遍历字符数组，挨个依据情况判断

    # 定义commad收集字符,commad初始化为空
    commad = ''
    # 定义commadList收集commad
    commadList = []
    for ch in s:

        # 如果当前ch是双引号，并且前面包含的双引号，那么就将当前的双引号添加到commadList列表中，置空commad
        if ch == '"' and '"' in commad:
            commad += '"'
            commadList.append(commad)
            commad = ''

        # 如果当前ch是_,并commad中不包含双引号，那么将commad添加到List中
        elif ch == '_' and '"' not in commad:
            commadList.append(commad)


        # 如果当前ch是最后一个字符,将当前ch加入commad,然后加入到commadList

        if
