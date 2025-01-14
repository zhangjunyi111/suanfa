# 3
# 12abc-abCABc-4aB@
# 改变心态，每个程序和功能都认真对待，不可以轻视和懈怠
# 改变心态，每个程序和功能都认真对待，不可以轻视和懈怠
# 改变心态，每个程序和功能都认真对待，不可以轻视和懈怠
# 改变心态，每个程序和功能都认真对待，不可以轻视和懈怠
# 改变心态，每个程序和功能都认真对待，不可以轻视和懈怠
# isupper函数判断字符串是否由大写字母组成
# islower函数
# upper函数将字符串转化为大写
# lower函数将字符串转化为小写



def count(s):
    '''
    统计一个对象中的数量，可以考虑用字典
    :param s:
    :return:
    '''
    char_dict = {}
    char_dict["upper"] = 0
    char_dict["lower"] = 0
    for char in s:
        if char.isupper():
            char_dict['upper'] += 1
        elif char.islower():
            char_dict['lower'] += 1

    return char_dict


def convert(s):
    upper_count = count(s)['upper']
    lower_count = count(s)['lower']
    if upper_count > lower_count:
        s = s.upper()
    elif lower_count > upper_count:
        s = s.lower()
    return s


def main():
    k = int(input())
    s = input().split('-')
    first_str = s[0]
    s_new = ''.join(s[1:])
    res = []
    for i in range(0, len(s_new), k):
        # 在区间内按区间遍历切割，区间为k的时候，判断 i+k的长度是否大于len(s)的长度就行。
        if i + k > len(s_new):
            children_str = s_new[i:]
            children_str = convert(children_str)
            res.append(children_str)
            break
        children_str = s_new[i:i + k]
        children_str = convert(children_str)
        res.append(children_str)
    print(first_str + '-' + '-'.join(res))


main()
