# 定义操作符列表
operators_list = ['+', "-", '*', '/']

# 创建2个栈，一个用于存储数字，一个用于存储操作符
numbers = []
operators = []

# 接收输入
s = input()


# 遍历输入字符串，注意弹出的顺序

def calc(numbers, operators):
    operator = operators.pop()
    num2 = numbers.pop()
    num1 = numbers.pop()
    if operator == '+':
        numbers.append(num1 + num2)
    elif operator == '-':
        numbers.append(num1 - num2)
    elif operator == '*':
        numbers.append(num1 * num2)
    else:
        numbers.append(num1 / num2)

# 定义操作符的优先级
def pri(c):
    if c in '+-':
        return 1
    elif c in '*/':
        return -1
    else:
        return 0


def caculate(s):
    """
    注意更新指针位置
    :param s:
    :return:
    """
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            numbers.append(int(s[i:j]))
            # 将 i移动到j的位置
            i = j

        elif c in operators_list:
            # 更新操作符的时候需要确保优先级大于站内的操作符，如果小于等于站内操作符的优先级，则弹出来，进行计算
            while operators and pri(c) <= pri(operators[-1]):
                calc(numbers, operators)
            operators.append(c)
            i += 1

        elif c == '(':
            operators.append(c)
            i += 1

        elif c == ')':
            while operators[-1] != '(':
                calc(numbers, operators)
            operators.pop()
            i += 1
        else:
            # 类似于空格这种字符，直接跳过
            i += 1
    while operators:
        calc(numbers, operators)
    return numbers.pop()


try:
    result = caculate(s)
except ArithmeticError:
    print('ERROR')
