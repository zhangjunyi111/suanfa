# 1-2abcd例子
# 0-9 数字+-*

# 算法思路
# 找出所有的表达式
# 比较长度
# 计算结果

def main():
    #    接收表达式字符串
    expression = input().strip()
    # 定义合法表达式的符号和数字列表
    legal_char_list = ['+', "-", "*"]
    legal_number = list(map(str, list(range(10))))
    # 定义合法的表达式列表
    legal_expression = []
    # 从左到右扫描表达式字符串
    i = 0
    while i < len(expression):
        # 当i为合法的数字或者符号的时候，开始统计表达式
        if expression[i]  in legal_char_list or expression[ i] in legal_number:
            # i为起点，移动j
            j = i
            while j < len(expression) and ( expression[j] in legal_char_list or expression[ j] in legal_number):
                    j += 1
                    # 更新i的值为j,从j开始继续找到第一个合法的表达式或者字符
            # 当j的值不满足合法表数字或者符号的时候，将i到j的区间的内容获取到，添加到合法表达式的结果中，等待进一步的处理
            legal_expression.append(expression[i:j])
            i = j
        # 不满足条件的话，i的值要+1，移动i指针
        else:
            i += 1
    length = 0
    index  = -1
    for i in range(len(legal_expression)):
        if len(legal_expression[i]) > length:
            length = len(legal_expression)
            index = i


    #  对表达式进行计算
    expression = legal_expression[index] if index != -1 else '0'
    #先计算乘法
    # 再计算加减法
    # print(expression)
    print(eval(expression))

main()
